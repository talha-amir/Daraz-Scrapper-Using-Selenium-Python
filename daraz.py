from os.path import isfile
from selenium import webdriver
import pandas as pd
from tqdm import tqdm
import argparse


class DarazScrapper:

    def __init__(self, category_name: str = "headphones-headsets", pages: int = float('inf')) -> None:
        self.file_name = f"daraz-{category_name}.csv"
        self.category_name = category_name
        options = webdriver.ChromeOptions()
        options.add_experimental_option('excludeSwitches', ['enable-logging'])
        options.add_argument("--disable-notifications")
        options.add_argument("--disable-popup-blocking")

        self.driver = webdriver.Chrome(
            executable_path="./Chrome Driver/chromedriver.exe", options=options)
        self.DATA = {"Link": [], 'Name': [], "Price": [], "Rating": [], "Total Ratings": [], "Image Links": [],
                     "Brand": [], "Brand Link": []}
        self.pages = pages
        self.exceptions = []

        self.to_csv(header=False if isfile(self.file_name) else True)

    def get_total_pages(self) -> int:
        return int(self.driver.find_element_by_xpath(
            "/html[1]/body[1]/div[3]/div[1]/div[3]/div[1]/div[1]/div[1]/div[3]/div[1]/ul[1]/li[8]/a[1]").text)

    def get_product_href(self, x) -> str:
        return x.find_element_by_class_name("cRjKsc").find_element_by_xpath(".//*").get_attribute('href')

    def append(self, link: str,
               name: str, price: int, rating: int, total_ratings: int, image_links: str, brand: str, brand_link: str) -> None:
        self.DATA['Link'].append(link)
        self.DATA['Name'].append(name)
        self.DATA['Price'].append(price)
        self.DATA['Rating'].append(rating)
        self.DATA['Total Ratings'].append(total_ratings)
        self.DATA['Image Links'].append(image_links)
        self.DATA['Brand'].append(brand)
        self.DATA['Brand Link'].append(brand_link)

    def extract_data_page(self, page: str = None) -> None:
        try:
            link = page

            self.driver.get(link)

            # get name
            name = self.driver.find_element_by_class_name(
                "pdp-mod-product-badge-title").text

            # get price
            price = eval(self.driver.find_element_by_class_name(
                "pdp-product-price").find_element_by_xpath(".//*").text.split()[-1].replace(',', ''))

            # get ratinngs
            rating = self.driver.find_element_by_class_name(
                "score").find_element_by_xpath(".//*").text

            # get total ratings
            total_ratings = self.driver.find_element_by_class_name(
                "pdp-review-summary").find_element_by_xpath("./a").text.split()[0]

            # get Image urls
            image_div = self.driver.find_element_by_class_name(
                "next-slick-track").find_elements_by_tag_name("img")
            image_links = ",".join(list(
                map(lambda x: x.get_attribute("src"), image_div)))

            # brand
            brand = self.driver.find_element_by_xpath(
                "//body/div[@id='container']/div[@id='root']/div[@id='block-o1b-XZ8ElL']/div[@id='block-Pvty24-PCy']/div[@id='block-gPt-1r6bsq']/div[@id='block-epgoLcDQG8I']/div[@id='module_product_brand_1']/div[1]/a[1]")
            brand_name = brand.get_attribute("innerHTML")
            brand_link = "-" if brand_name == "No Brand" else brand.get_attribute(
                "href")
            self.append(link,
                        name, price, rating, total_ratings, image_links, brand_name, brand_link)

        except Exception as error:
            self.exceptions.append(str(error))
        except KeyboardInterrupt:
            exit(-1)

    def main(self):
        self.driver.get(f"https://www.daraz.pk/{self.category_name}")
        total_pages = self.get_total_pages()
        print(f"Category = {self.category_name}")
        print(f"\nTotal Pages : {total_pages}")
        total_pages = total_pages if self.pages >= total_pages else self.pages
        print(f"Number of pages to Extract : {total_pages}")
        for i in (range(1, total_pages+1)):
            self.driver.get(
                f"https://www.daraz.pk/{self.category_name}?page={i}")
            divs = self.driver.find_elements_by_class_name("c2prKC")
            hrefs = list(map(self.get_product_href, divs))
            print(f"Extracting Page : {i}")
            for i in tqdm(range(len(hrefs))):
                self.extract_data_page(hrefs[i])
            self.to_csv()
            self.exceptions_to_file()
        self.driver.quit()
        print("Data Extracted !!.")

    def exceptions_to_file(self) -> None:
        if not len(self.exceptions):
            return
        with open('logs.txt', mode="a") as file:
            file.writelines(self.exceptions)
        self.exceptions = []

    def to_csv(self, header=False):

        pd.DataFrame(self.DATA).to_csv(self.file_name,
                                       index=False, mode='a', header=header)
        self.DATA = {"Link": [], 'Name': [], "Price": [], "Rating": [], "Total Ratings": [], "Image Links": [],
                     "Brand": [], "Brand Link": []}


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Scraps product data from Daraz for a s specific category")
    parser.add_argument(
        '--pages', type=int, help="Total Number of Pages to Scrap Leave Empty for max pages", default=float('inf'))
    parser.add_argument(
        '--category', type=str, help="Name of Sub-Category to Scrap Leave Empty for Default", default="headphones-headsets")
    args = parser.parse_args()

    DarazScrapper(pages=args.pages, category_name=args.category).main()
