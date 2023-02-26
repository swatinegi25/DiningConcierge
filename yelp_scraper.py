import requests
import json

restaurants = []
cuisines = ['Chinese', 'Indian', 'Italian', 'Japanese', 'Korean', 'Greek', 'Mexican', 'Mediterranean', 'French', 'American']

for cuisine in cuisines:
    for offset in range(0,500,50):

        url = "https://api.yelp.com/v3/businesses/search?location=Manhattan&term=" + cuisine + "%20restaurants&categories=&sort_by=best_match&limit=50&offset="+str(offset)

        headers = {
            "accept": "application/json",
            "Authorization": "Bearer 5d3M1f5_2BLr3KGfwFfxZqMJAl-LYFx8NEWuJ_6waaatVublla4ekwvBskK-cNtnIbR7pByPcXjVvz8sFDxiEnrRPeY5k9n4EEBgM0Klw674eU_HjM7O18NBe-ryY3Yx"
        }

        response = requests.get(url, headers=headers)
        response = response.json()



        for business in response['businesses']:

            restaurants.append({
                "BusinessID": business['id'],
                "Name": business['name'].replace("'", ""),
                "Address": business['location']['address1'],
                "Coordinates": business['coordinates'],
                "Number of Reviews": business['review_count'],
                "Rating": business['rating'],
                "Zip Code": business['location']['zip_code'],
                "Cuisine": cuisine
            })

        print("Offset " + str(offset))
    print("Done " + cuisine)

f = open("restaurants.txt", "w")
f.write(str(restaurants))
f.close()