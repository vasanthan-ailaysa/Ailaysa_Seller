# Ailaysa Book Sellers Page

## Requirements Specification

### Data Requirements
#### Entities and Attributes
  - user 
    - name
    - email
    - password
    - staff_id
  - book
    - title
    - author
    - publisher
    - isbn
    - language
    - genre
  - author
    - name
    - about
  - publisher
    - name
    - address
    - country

#### Relationships
- user - publisher (many to one)
- book - publisher (many to one)
- book - author (many to one)




### Functional Requirements
- staff user must be able to register, login, and logout form the app
- staff user must be able to perform crud operations on the book data owned by their publication


### Non Functional Requirements


## Testing


## Deployment


# Todo

- user authentication and authorisation api
- Book seller API
- test cases
- frontend
- deployment
- documentation