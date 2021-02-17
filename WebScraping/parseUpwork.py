from bs4 import BeautifulSoup as bs


def extract_info(raw_html):
    user_data = {
        "notification_count":None,
        "visibility":None,
        "availability":None,
        "proposals":None,
        "categories":[]
    }

    with open('captured_pages/main_page.html','r',encoding='utf-8') as infile:
        soup = bs(infile.read(), 'html.parser')
        user_data["notification_count"] = soup.find("li",{"data-cy":"notifications-link"}).text
        user_data["visibility"] = soup.find("fe-profile-visibility")
        user_data["availability"] = soup.find("div", {"class":"fe-ui-availability"}).text
        user_data["proposals"] = soup.find("fe-fwh-proposal-stats").text
        user_data["categories"] = soup.find("fe-fwh-my-categories").find_all("li")
        return user_data

#document.querySelector("li[data-cy='notifications-link'] span span span").textContent.trim()

if __name__ == "__main__":
    pass