import pandas as pd
import sklearn
import itertools
# import numpy as np
# import seaborn as sb
import re
import nltk
import pickle
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import  MultinomialNB
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score ,confusion_matrix ,classification_report
# from sklearn import metrics
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import GridSearchCV
from sklearn import metrics
import numpy as np
# from sklearn.metrics import confusion_matrix
from matplotlib import pyplot as plt
from sklearn.linear_model import PassiveAggressiveClassifier
from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords

print("25%")

data = pd.read_csv('fake_job_postings_cleaned_2.csv')

# print(stopwords.words("english"))

stop_words = set(stopwords.words("english"))

data['text'] = data['text'].apply(lambda x:x.lower())

data['text'] = data['text'].apply(lambda x:' '.join([word for word in x.split() if word not in(stop_words)]))

# data['text'][0]

X_train,X_test ,y_train,y_test = train_test_split(data.text, data.fraudulent ,test_size =0.3)

vect = CountVectorizer()
vect.fit(X_train)

# Convert the text data into vector format 
X_train_dtm = vect.transform(X_train)
X_test_dtm = vect.transform(X_test)

print("50%")

# Decision Tree Classifier

dt = DecisionTreeClassifier()
dt.fit(X_train_dtm,y_train)

y=data.fraudulent
# print(y.head())

X=data.drop('fraudulent',1)
# print(X.head())

X_train, X_test, y_train, y_test = train_test_split( X, y, test_size=0.3, random_state=4)

input_text = ['general laborers us, ct, hartford elite environmental group llc. provides staffing services temporary employment opportunities wide range clients, business owners search employees, candidates search employment environmental, construction industry. elite environmental group currently hiring general laborers, construction, housekeeping, manufacturing associates temporary temporary hire positions, paying $9.00 - $13.00 per hour. you’re dependable looking work, contact elite environmental group today. job descriptionconstruction erect dismantle scaffolding, shoring, braces, traffic barricades, ramps, temporary structuresmanufacturing associate receive count stock items, record data manually using computer.general labor clean prepare construction sites eliminate possible hazards.pack unpack items stocked shelves stockrooms, warehouses, storage yards.housekeeper clean guest rooms common areasmark stock items using identification tags, stamps, electric marking tools, labeling equipment. ideal candidatesrelevant experience preferredreliable transportationcommitted safety timesexcellent attendance']

input_data = vect.transform(input_text)

prediction = dt.predict(input_data)

if (prediction[0] == 1):
  print("This advertisement belonging to fake job post category")
  
else:
  print("This advertisement belonging to real job post category")  

print("75%")

def remove_stopwords(text):
    global filter_2
    stop_words = set(stopwords.words('english'))
    words = nltk.word_tokenize(text)
    filtered_words = [word for word in words if word.lower() not in stop_words]
    filter_2 = ' '.join(filtered_words)

def faker(some_input):
    
    review = some_input

    some_input = re.sub(r'[^a-zA-Z\s]', '', some_input)

    some_input = some_input.lower()

    remove_stopwords(some_input)

    input_data = vect.transform([filter_2])

    prediction = dt.predict(input_data)

    if (prediction[0] == 1): 
        return False
    #"This advertisement belonging to fake job post category"
    
    else:
        return True
    #"This advertisement belonging to real job post category"  

# faker("Web Application Developers NZ, N, Wellington Engineering Vend is looking for some awesome new talent to come join us. You'll be working in an awesome team doing awesome things, and generally being awesome.Learn about us on ourÂ blog, or meet the team onÂ Twitter,Â Facebook,Â LinkedInAwesome SpaceOur brand new Auckland office space is located on Nuffield Street in Newmarket, surrounded by our customers and the industry we love. It is huge, open, and shiny new with great meeting room spaces, casual working environments and plenty of space to host awesome events. We don't do cubicles, just plenty of space, whiteboards and meetings rooms. We also have a great cafe/retail space with our very own Front of House Manager taking care of our visitors and fellow Venders.Â Like Auckland our Melbourne office is surrounded by retail. It's a great wee space equipped with tiny houses and some awesome cardboard cutout animals.Our Toronto office is located right in the heart of downtown retail district. Like Melbourne and Auckland there's a great vibe with great coffee, boutique stores and some of the greatest restaurants in the city.Â Our SoMa office in San Francisco is located in the middle of the SF tech scene, just a (Biz) stone's throw from Twitter.The EnvironmentWe want you to be at the top of your game. You can wear whatever clothing you like, start work late in the morning, take breaks whenever you want and generally work the way you want to work.Â Who we're looking forVend is looking for people to push the boundaries. We are a hard working professional team with a wicked sense of humour, and we are looking for people who thrive in a collaborative open environment. We want passionate, hard working, talented individuals that want to lead in their field. Who are we?Vend is an award winning web based point of sale software for retail.Â  Weâ€™re chucking out crusty old cash registers and replacing them with iPads, touch screens and beautiful software, all of this to make life easier for our retailers.Â  Vend is a fast-growing tech start-up, since launching in 2010 weâ€™ve now got 10,000+ customers all over the world and have more than 100 employees.Â In case youâ€™re interested in our tech stack we use Capistrano, Redis, Git / Github, Vagrant, Jenkins, Puppet, Resque, New Relic, Doctrine, MySQL, Objective C, PHP, JavaScript, GO, Symfony, Rake, Selenium, Compass, SASS, jQuery, Bundler, Nginx, and a bunch of other things.Why youâ€™d like us:Our engineering department houses some of the smartest minds in NZ, they work tirelessly with our product teams to come up with the best and brightest new features and fixes for the Vend platform. As you can see from our tech stack above, we use the latest and greatest to bring delight to our customers, and want to add members to our team that live and breathe technology just like we do.As well as developing a world-leading product, we believe that our culture is world-leading too! We balance super hard work with having a lot of fun at work! Â Like playing pool, getting a Dia de los Muertos makeover, zoning out on the couches listening to music or raiding the snack cupboard (FYI frozen marshmallows are the latest craze at Vend - seriously, try them!).Â Work-life balance. Â We know you have a life outside of work. We know you probably have little side projects or businesses too. This is valued and at Vend you can have a life inside work to. Weâ€™ll also give you a $5,000 allowance per year to develop your skills and attend conferences of your choice. Within reason, of course. We turned down the guy who wanted to use the five large to go to aÂ heavy metal concert on a cruise ship.Â  We want to hear from you if:You have an in-depth understanding of OO programmingYou totally get MVC and multi-tier architectureYou have experience with TDD or writing automated testsYou understand relational databases and know how to write SQLYouâ€™ve worked an Agile-style team before and are down with cooperationBonus points if youâ€™ve worked in retail beforeIf this sounds like you then get in touch now and delight us with your unique application! We have HUGE projects in the pipeline this year and need the best talent on-board to help achieve our goals.While Vend is totally open to receiving applications from people based overseas, our recruitment process for technical talent is lengthy and involves a lot of face-to-face time between our candidates and existing team members here. We can start initial stages of interviewing using awesome technology like Skype and Google Hangouts, we really need you to be here and to have hung out with us in Auckland before making a job offer.   Computer Software")