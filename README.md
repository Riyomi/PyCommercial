# [PyCommercial](https://pycommercial.herokuapp.com/home/)

## Introduction

PyCommercial is a webshop app created with Django, TailwindCSS with a hint of Javascript/JQuery. Users can browse / review products, add them to their carts and place orders.

## Note (important)

The app is deployed with a **free** Heroku account, so loading it for the first time might take up to 10 seconds until the web process wakes up.

## The objectives of this project

Brush up my CSS skills (the main focus being on reviewing the use of flexbox, grid and media queries), learn Django, try out TailwindCSS in a bigger project and review the deployment process to Heroku.

## Tech used

- HTML
- CSS (flexbox, grid, media queries)
- Python
- Django
- Javascript
- JQuery
- AJAX requests

## Future development

- **Redo the frontend design:** looking back now (at the time I'm writing this, it's been two months after I finished this project), the frontend design is severly lacking, so in the future, I'd like to revisit this project to give it a fresh and modern look.
- **Replace Tailwind with pure CSS:** long story short, now I don't think Django (when using it to generate pages server-side) and TailwindCSS are a good match. Using TailwindCSS made reading and understanding the templates harder since it's not obvious at first glance what certain divs represent. A good example for this is `<div class="px-4 w-screen desktop:w-full">` which is supposed to be the div where recommendations are shown on the homepage. I could have of course exported this as a Tailwind class and name it "homepage-recommendations" but that would've defeated the whole purpose of using TailwindCSS in the first place. I believe TailwindCSS has its own uses with frontend frameworks like React, Vue or Angular where everything is divided into different components which makes coming up with CSS classnames somehow redundant and unnecessary, but for this project, now I'm convinced that it wasn't the best choice.
