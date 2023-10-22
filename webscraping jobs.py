import bs4, requests

base_url = "https://realpython.github.io/fake-jobs/"

applicants = []

results = requests.get(base_url)
soup = bs4.BeautifulSoup(results.text, "lxml")
content = soup.select(".card-content")


def results():
    counter = 0
    length = 0
    print("-"*82)
    for i in applicants:
        print(f"\n{i}\n")
        counter += 1
        if counter == 3:
            length += 1
            counter = 0
            print("-"*82)
    print(f"{length} profiles have been found ")


def again():
    another_try = input("Do you want to look for another profile? ").lower()
    return another_try


def profile():
    
    while True:
        name = input('Please enter a profile: ')
        if not name.replace(' ', '').isalpha():
            print('Please enter a alphabetical profile')
        else:
            return name


def search():

    while True:
        applicants.clear()
        objective = profile().lower()
        
        for i in content:
            direct_search = i.select("h2")[0].text.lower()
            if objective in direct_search:

                titles = i.select("h2")[0].text
                applicants.append(titles)

                names = i.select("h3")[0].text
                applicants.append(names)

                links = i.select('a')[1]['href']
                applicants.append(links)

        if len(applicants) != 0:
            results()
            another_try = again()

        else:
            print('Profiles not found')
            another_try = again()

        if another_try == 'yes':
            continue

        else:
            break


search()

