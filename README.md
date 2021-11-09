# closest-nhs

A utility to get the closest NHS location: GPs, Dentists, Pharmacies etc

# Set-up

_Working as of: 9th Nov 2021_

1. Create a NHS [developer account](https://developer.api.nhs.uk/register)
2. Then go to your dev account [profile](https://developer.api.nhs.uk/profile) & copy your Primary key
3. Paste your key into a .env file at the root of this project. You can do this using `echo "your primary key" > .env` - of course replace text in quotes with your personal key.

**OR**

1. Type `make setup` in root folder of project

# Todo

- [x] Get JSON from NHS API
- [ ] Parse JSON data into readble results
- [ ] Accept search query as user input
- [ ] Allow user to select what Organisation type to search for.
- [ ] GUI
