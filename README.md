### Just a simple POC of a script for generating out-of-stock list for a pharmacy.

Supplied with two excel files, it extracts the common and uncommon items between both and generates two excel files respectively.

#### Usage
After cloning repo, cd into directory and run `pip install -r requirements.txt`

Code can be run via the script or using the CLI app as thus: `python pro.py generator [Path to wholesalers list] [Path to your list]`. 

For example, run `python pro.py generator sample_wholesaler.xlsx sample.xlsx`.

For full understanding of CLI app, run `python pro.py generator -h`
