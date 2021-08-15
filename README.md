![Karma Yoga Logo](read-me/readme-logo.png)

Karma Yoga is an e-commerce web application developed as part of 
[*Code Institute, Diploma in Full Stack Software Development*](https://codeinstitute.net/full-stack-software-development-diploma/).
It is the final milestone project in a series of four projects.

The live site can be accessed [*here*](INSERT HERE).

*Please note: To open any links in this document in a new browser tab, please press `CTRL + Click`.*

## Table of Contents
1. [Strategic Purpose Overview](#strategic-purpose-overview)
    * [Design Simulation](#design-simulation)
2. [User Experience Design](#user-experience-design)
   * [User Stories](#user-stories)
    *  [Design](#design)
        * [Scope and Structure](#scope-and-structure)
        * [Wireframes](#Wireframes)
        * [Database Structure](#database-structure)
        * [Security](#security)
        * [Color Scheme](#color-scheme)
        * [Typography](#typography)
        * [Imagery](#imagery)
3. [Features](#features)
    * [Existing Features](#existing-features)
    * [Future Features](#future-features)
4. [Technologies](#technologies)
    * [Languages](#languages)
    * [Frameworks and Libraries](#frameworks-and-libraries)
    * [Programmes and Tools](#Programmes-and-tools)
    * [Sources](#sources)
5. [Testing](#testing)
    * [Code Validity](#code-validity)
    * [Testing Premise](#testing-premise)
    * [Functionality](#functionality)
    * [Bugs and Fixes](#bugs-and-fixes)
    * [Final Comments](#final-comments)
6. [Deployment](#deployment)
    * [Deployment via Heroku](#deployment-via-heroku)
    * [Make a clone on GitPod](#make-a-clone-on-gitpod) 
7. [Credits](#credits)
    * [Images](#Images)
    * [Code](#Code)
    * [Content](#Content)
    * [Acknowledgements](#Acknowledgements)
## Strategic Purpose Overview

Karma Yoga is a full stack e-commerce web application for a theoretical yoga studio. The site as well as being an informative marketing tool, also facilitates the sale of class passes and yoga equipment available at the studio. Consumers will be able to purchase class passes to allow them entry to class or purchase equipment they may require for their yoga practice. Registered users will be able to save, update and delete their information and view past orders on a profile, as well as save their favourite products/passes for ease of access in the future. The site will also facilitate a means of contact to the studio via a contact form. The administrator will be able to update, edit and delete products from the frontend and monitor orders and users information from the backend.

Karma Yoga is a fully responsive data driven application using HTML, CSS, JavaScript, Python, Django Frameworks, a Postgres relational database and Stripe Payment technology. The user interface is based on the principles of good UX design. The application is cloud hosted via AWS and Heroku.

### Design Simulation

A simulation of the website on desktop and mobile devices can be seen below.

![Design Simulation]()

 The live site can be accessed [*here*]().

*Please note: To open any links in this document in a new browser tab, please press `CTRL + Click`.*

## User Experience Design

### User Stories

#### Anonoumous User

| **As an anonoumous I would like to ** : |  **So that I can**  : |
| ------------- |:-------------:|
| easily understand the main purpose of the site | determine if it is what I need |
| use an aesthetically pleasing site| enjoy my user experience |
| easily navigate the site| quickly find what I need |
| find information is clearly presented | absorb it with minimal effort |
| view the site on different screen sizes| use it on a desktop or on the go |
| view/search products and class passes | find items quickly |
| purchase products/class passes online | save time & travel expense |
| contact the studio on their site | enquire without opening a secondary platform |

#### Registered User

A registered users goals are in addition to the above mentioned user goals.

| **As a registered user I would like to ** : |  **So that I can**  : |
| ------------- |:-------------:|
| save my information to a profile | use it again easily |
| edit/delete my profile | manage my information |
| view past orders | keep track of them |
| be able to favourite items to my profile | access them easily for re-purchase or review |

#### Business Objective / Admin User

| **As an admin user I would like to ** : |  **So that I can**  : |
| ------------- |:-------------:|
|  have an informative web application | use it as a marketing tool |
|  sell products and class passes | generate revenue |
|  have a record of user/student information | use it for marketing and other business purposes |
|  have a contact form on the app | manage enquiries via email only |
|  upload, edit and delete products through the frontend | manage stock and product/service offering over time |

## Design

### Scope and Structure

**Scope**

* Responsive Design 
* Informative Landing Page
* Sticky top Nav Bar & Mobile Nav Bar 
* Relational database to store all uploaded data/content
* CRUD functionality for profiles and products
* Authentication functionality
* Profile page
* Search functionality
* Contact functionality
* E-Commerce functionality

**Skeleton Structure**

This application will be made up of 11 "pages" derived or based around 4 data models, product/class pass, user profile, contact form and favourites.

The landing page will consist of a large hero image with a text introduction of the site's offering or purpose.

Login, registration, add/edit products/profile and contact pages will all consist of forms with varying inputs dependant on the purpose of the form.

The profile page will display user information derived from the form, past orders and favourite products/class passes with options to edit or delete all information or favourites.

The products page will display all products/class passes and be searchable.

The product detail page will display the image and details with an option to purchase or update/delete for the admin user.

**Interaction Design**

The nav bar items will highlight on hover.

The user will be able to interact with the data on the application via the search bar, products will display below the search bar if found or a message with an error if not found.

All forms will validate and change colour/display messages to notify the user of errors.

Successful actions and unsuccessful actions will be flagged with django messages to the user.

### Wireframes
A mock-up of how the site will be laid out is available here via [Wire Frames](read-me/booknook.pdf).

### Database Structure

![Database Structure]()

TBC

### Security

Sensitive data such as SECRET_KEYS were stored on heroku using config variables to prevent unwanted connections to the database.

Django allauth was used to set up user authentication and built in decorators allowed restricted access to certain features on the website.

### Color Scheme

![Color Swatch](read-me/color-swatch.png)

The above color swatch shows a guideline for the color scheme of the site.

Colors are brand colours that have been adopted for their strong visual contrast in an attempt to make all content as easily consumable and suitable for visually impared users as possible.

### Typography

The Courgette font, created by *Karolina Lach* for [Google Fonts](https://fonts.google.com/specimen/Courgette?preview.text=CROSSFIT&preview.text_type=custom&query=cour#about) will be the main font for all headings in style 400 regular. 

The Libre Baskerville font, created by *Impallari Type* for [Google Fonts](https://fonts.google.com/specimen/Libre+Baskerville?preview.text=CROSSFIT&preview.text_type=custom&query=libre#about) will be the main font for all other content in style 400 regular. 

![Courgette Font](read-me/font-sample-one.png)

![Libre Baskerville Font](read-me/font-sample-two.png)

### Imagery

Black and white imagery is used for hero and background images to keep inline with the theme of the app, images are from open sourced platforms.

The logo and class passes were created using [canva.com](https://www.canva.com/).

Product images are from [alibaba.com](https://www.alibaba.com/).

For a detailed list of image sources please see the [credits](#credits) section.


## Features

1. Responsive to different screen sizes.
2. Supported by Chrome, Microsoft Edge, and Firefox browsers.
3. Adapted for users with special accessibility requirements where possible.
4. There will be 14 pages: Landing page, all products page, categorized product page, product detail page, shopping bag, checkout page, successfull check out page, profile page, login page, sign up page, delete/edit product page, contact form page, 404 error and 500 error page.

        - Each page will have a navigation header
        - Each page will have a footer
        - Each page will have a favicon on the browser tab

5. Each page will have a 'sticky' navbar

        - White with black text or the reverse
        - Text logo on the left, or removed on smaller screens
        - a central search bar
        - Menu options in the center or to the left on mobile
        - The logo will route back to the home page
        - Menu options will change to color on hover & envoke a pointer
        - On mobile devices, the menu items will switch to a toggle button and slide down the page when button is clicked
        - The mobile nav will not have 'on-hover' styling
        - Anon users will see my account(signup/register), search bar, shopping cart total, all products, contact page, equipment and classes page 
        - Registered users will see the above mentioned with an additional profile tab and log out option under the 'my account' nav item

 6. The home page will have:

        - A hero image.
        - Informative text

7. The login/register page will have:

        - A form requesting user information (name, username & password) and a submission button

8. The profile page will have: 

        - An area displaying the users information
        - An area displaying orders the user has purchased
        - There will be an option to edit/delete information
        - A favourites section

9. The all products page will have:

        - A sort by category bar
        - A section displaying existing products and class passes
        - Each product will have an image, label and a link to review its details
        - To an admin user there will be a link to edit/delete

10. The product detail page will have:

        - An image of the product
        - Descriptive text
        - Price
        - Quantity selector
        - Add to cart button
        - Go back button
        - Edit/Delete link for the admin user only
        - Messages displaying successfull addition of products to the shopping bag

11. The shopping bag page will have:

        - Images and descriptions of products
        - Option to edit quantity or remove products, with messages conveying these actions
        - Grand total calculation
        - Keep shopping button
        - Continue to checkout button

12. The check out page will have:

        - A form requesting order details
        - An order summary
        - A stripe payment option
        - A check box to save info to a profile
        - A grand total
        - Messages to convey successful or unsuccessful check out

14. The categorized product page will have the same features as the 'all product page' but will be pre filtered to that specific category.

15. The contact form page will have a form with fields for:

        - Name
        - Email
        - Drop down for book a class, gen enquiry or my orders
        - Text box

16. All users interactions will either be confirmed or notified of an error eith via on screen messages, orders and profile set up will be also confirmed via email.
### Future Features

Future features will include:

>   * An online booking system
>   * A chat forum for members of workshops or training courses at the studio

