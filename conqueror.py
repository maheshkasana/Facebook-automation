from selenium import webdriver
from termcolor import colored
import pickle
import os
import time
credential_dict = {}


def delete_facebook_account():
    global credential_dict
    print("Welcome To Remove Facebook user credentials ")
    username = input("Enter Username : ")
    credential_dict.pop(username, 0)
    os.remove("conqueror_credential")
    dbfile = open("conqueror_credential", "ab")
    pickle.dump(credential_dict, dbfile)
    dbfile.close()


def add_facebook_account():
    global credential_dict
    print("Welcome TO Add new Facebook user credentials ")
    username = input("Enter Username : ")
    password = input("Enter Password : ")
    if username in credential_dict:
        print(colored("Username Already Exits : ", "yellow"))
        return
    credential_dict[username] = password
    os.remove("conqueror_credential")
    dbfile = open("conqueror_credential", "ab")
    pickle.dump(credential_dict, dbfile)
    dbfile.close()


def load_credential_dict():
    global credential_dict
    dbfile = open("conqueror_credential", "rb")
    credential_dict = pickle.load(dbfile)
    dbfile.close()


def update_credentials():
    global credential_dict
    print("\nWelcome To Update Credentials of Facebook")
    username = input("Enter Username : ")
    password = input("Enter Password : ")
    credential_dict[username] = password
    os.remove("conqueror_credential")
    dbfile = open("conqueror_credential", "ab")
    pickle.dump(credential_dict, dbfile)
    dbfile.close()


def print_current_credentials():
    print("\n\nCurrently Present Username & Password")
    if len(credential_dict) == 0:
        print(colored("No Credentials Present :)", "red"))
        return
    i = 1
    for user, psw in credential_dict.items():
        print(colored(" {0} : {1} , {2}", "green").format(i, user, psw))
        i += 1


def logout_from_facebook(window_chrome):
    window_chrome.find_element_by_id("pageLoginAnchor").click()
    time.sleep(2)
    window_chrome.find_element_by_css_selector("._w0d[action='https://www.facebook.com/logout.php?button_name=logout&button_location=settings']").submit()


def send_friend_requests(window_chrome):
    print("\n\nWelcome to module to send friend requests")
    # window_chrome.find_element_by_xpath("//*[contains(@id, 'profile_pic_header_')]").click()
    # window_chrome.find_element_by_class_name("_2s25 _606w").click()
    window_chrome.find_element_by_xpath('//*[@title="Profile"]').click()
    time.sleep(5)
    window_chrome.find_element_by_link_text("Friends").click()
    time.sleep(5)
    window_chrome.find_element_by_link_text("Find Friends").click()
    print("Mahesh")
    """ this one is for seleting the Hometown or Current city or Mutual friend
    print(colored("Enter No for each field which you doant want to use", "red"))
    current_city = input("Enter The Current location : ")
    hometown = input("Enter The Home Town : ")
    mutual_frnd = input("Enter the name of Mutual Friend : ")
    if current_city != "No":
        # window_chrome.find_element_by_id("u_jsonp_4_75y").send_keys(current_city)
        # window_chrome.find_element_by_id("u_jsonp_4_7y").submit()
        window_chrome.find_element_by_xpath('//*[@placeholder="Enter another city"]').send_keys(current_city)
        window_chrome.find_element_by_xpath('//*[@placeholder="Enter another city"]').submit()
        time.sleep(5)
    if hometown != "No":
        # window_chrome.find_element_by_id("u_jsonp_4_7w").send_keys(hometown)
        # window_chrome.find_element_by_id("u_jsonp_4_7w").submit()
        time.sleep(5)
    if mutual_frnd != "No":
        # window_chrome.find_element_by_id("u_jsonp_4_82").send_keys(mutual_frnd)
        # window_chrome.find_element_by_id("u_jsonp_4_82").submit()
        time.sleep(5)
    """
    # all_add_frnd = window_chrome.find_elements_by_link_text("Add Friend")
    # print(type(all_add_frnd))
    # print(len(all_add_frnd))
    # window_chrome.find_element_by_link_text("Add Friend").click()
    all_add_frnd = window_chrome.find_element_by_xpath("//*[contains(text(), 'Add Friend')]")
    all_add_frnd[0].click()



def accept_all_friend_requests(window_chrome):
    print("\n\nWelcome to module to Accept All friend requests")
    return
    # window_chrome.find_element_by_xpath("//*[contains(@id, 'profile_pic_header_')]").click()
    # window_chrome.find_element_by_class_name("_2s25 _606w").click()
    # #window_chrome.find_element_by_xpath('//*[@title="Profile"]').click()
    # window_chrome.set_page_load_timeout(10)
    # #window_chrome.implicitly_wait(10)
    # #window_chrome.find_element_by_link_text("Friends").click()
    # window_chrome.set_page_load_timeout(10)
    # #window_chrome.refresh()
    # #window_chrome.implicitly_wait(10)
    # #window_chrome.refresh()
    # #time.sleep(5)
    # #window_chrome.find_element_by_link_text('::before'"Friend Requests").click()
    # window_chrome.set_page_load_timeout(10)
    # #window_chrome.refresh()
    # #window_chrome.implicitly_wait(10)
    # #window_chrome.refresh()
    # #time.sleep(5)
    window_chrome.find_element_by_id("js_2iq").click()

    all_request = window_chrome.find_elements_by_link_text("Confirm")
    j = 1
    for i in all_request:
        print(i.location)
        print(i)
        print(j, end='\n\n')
        j += 1


def login_to_facebook_account():
    print("\n\nWelcome To Login Module\nEnter The index relative to Username you want to login")
    print_current_credentials()
    option = int(input())
    if option > len(credential_dict) or option <= 0:
        print(colored("Enter index in limit, out of scope index entred", 'red'))
        return
    i = 1
    for username, password in credential_dict.items():
        if i == option:
            break
        i += 1

    window_chrome = webdriver.Chrome("C:\\webdriver\\chromedriver.exe")
    window_chrome.get("https://www.facebook.com")
    window_chrome.maximize_window()
    window_chrome.set_page_load_timeout(20)
    window_chrome.find_element_by_id("email").send_keys(username)
    window_chrome.find_element_by_id("pass").send_keys(password)
    window_chrome.find_element_by_id("u_0_2").click()
    while True:
        print("\n\n\tWelcome To perform operation :\n\t0 : Logout & Exit\n\t1 : Send Friend Requests\n\t2 : Accept All Friend Requests\n")
        option = int(input("\t"))
        if option == 0:
            logout_from_facebook(window_chrome)
            window_chrome.close()
            break
        elif option == 1:
            send_friend_requests(window_chrome)
        elif option == 2:
            accept_all_friend_requests(window_chrome)


def main():
    global credential_dict
    try:
        dbfile = open("conqueror_credential", 'rb')
        try:
            credential_dict = pickle.load(dbfile)
            dbfile.close()
        except EOFError:
            credential_dict = {}
    except FileNotFoundError:
        dbfile = open("conqueror_credential", 'ab')
        pickle.dump(credential_dict, dbfile)
        dbfile.close()

    while True:
        print("\n\nWelcome To Main Menu :\n0 : Exit\n1 : Add New Facebook Account\n2 : Remove Facebook Account List"
              "\n3 : Print Credentials in list\n4 : Update The Credentials in list\n5 : Login To account")
        option = int(input())
        if option == 0:
            break
        elif option == 1:
            add_facebook_account()
            load_credential_dict()
        elif option == 2:
            delete_facebook_account()
            load_credential_dict()
        elif option == 3:
            print_current_credentials()
        elif option == 4:
            update_credentials()
        elif option == 5:
            login_to_facebook_account()

#MAhesh Kasana
if __name__ == '__main__':
    main()
