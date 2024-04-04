# Clipboard History

this project gives users who can 
only copy and paste one item at a 
time an easy solution to that problem



after running git clone https://github.com/shmulisarmy/clipboardHistory.git run: 
```sh
pip install -r requirements.txt
```
to download all the dependencies

## load.py

while running, every 5 seconds it 
will check if anything new has been 
pasted and if so it will add it to 
the jason file 

```sh
python3 load.py
```

## get.py

gives the user an easy way to 
copy data from the json file  
into clipboard

```sh
python3 get.py
```
