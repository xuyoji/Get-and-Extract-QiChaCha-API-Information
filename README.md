# Function
* Use Qichacha's API to get company information
* Convert them to csv file

# How to use
Basically, there's already two defaults APIs *GetDetailsByName* and *GetDetailsByName*.
You can add or delete them.
## Get raw information
1. Get your API keys from QiChaCha and type in them in **key.py**.
2. Get API domenstration information in correspond website of QiChaCha.(Note I find a bug in its URL, the flag to indicate keyword may differ. In the given two default APIs, they are 'keyword' and 'searchKey'. You should get your own one by QiChaCha's URL example.)
3. Edit **crawl.py** to give the API information to the program.
4. Export the company list you want to get information in **csv** file information by excel. Name it **companyList.csv** in the same directory of the program.
5. Run **crawl.py**. The information will saved in the correspond folder.
## Process the information
1. Write the information you want to extract in the format of example in **process.py**.
2. Modify the example code to adapt to your information.


