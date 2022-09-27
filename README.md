# [**CNEbroidery**](https://https://cnembroidery.herokuapp.com/)

![Portfolio image](media/home-page.jpg)

## **Overview**

This is an e-commerce web application complete with product search and filter functionality. A live fully functional payment system. A full-featured authentication system including email confirmations and user profiles. And real-time notifications that guide the user's experience. The website was built in modern software development Such as Stripe, Amazon Web Services, Heroku, and more.

## **Table of Contents**

- [**CNEbroidery**](#overview)
  - [**Overview**](#overview)
  - [**Table of Contents**](#table-of-contents)
    - [**1. What Is It?**](#1-what-is-it)
    - [**2. How to Achieve?**](#2-how-to-achieve)
    - [**3. Testing and Launch**](#3-testing-and-launch)
    - [**4. Deployment**](#4-deployment)
    - [**5. Support**](#5-support)
    - [**6. Reference and Research**](#6-reference-and-research)

### **1. What Is It?**

- CNEbroidery
[Details of Ebroidery described on Wiki](https://en.wikipedia.org/wiki/Chinese_embroidery)

The name CNEbroidery is a combanation of 'CN' and 'Ebroidery', Chinese Ebroidery has been popular in China for thousands of years，most of the Chinese embroideries are made of silk. It is commonly made by hand, especially for very sophisticated design. It's considered as one of best gifts or collections. This website is built to introduct Chinese Ebroidery and sell high quality Chinese Ebroidery. 

[Back to the top](#overview)

### **2. How to Achieve?**

- Home page

  - **Welcome Page**

  ![Welcome-page](media/home-page-intro.gif)

  - Nav bar
    - ***CNEbroidery***: clicking website name will be redirected back to the home page.
    - ***My account***: allowing users to login or sign up.

    ![Login and Sign Up](media/login-signup.gif)
    
    - ***Products***: users can access product page by clicking 'shop now' button or via nav product link. It contains all products link and individual product categories. There are three categories which are Decoration, Fashion and Offers.

    ![Products-page](media/product-page.gif)

    - ***Search engine and sorting products***: users are able to search from the entire site or sort by product size from small to big or sort by product price from low to high.
    - ***Cart***: the color of cart icon will change to blue if users have added any items to cart. The total amount of shopping also availiable there. Clicking 'View Cart' will direct our users to cart detail page.

  - Footer
    - ***Subscribe***: users can enter an email to subscribe monthly newsletter to get exclusive offers and discount codes.
    - ***Facebook Social Link***: Facebook is used to build a community and deepening relationships with customers to encourage interest and customer loyalty.
    - ***Privacy Policy***: Privacy Policy to display to make sure that business complies with the law.


- **Program flow chart**

    ![Flow Chart](images/flow-chart.jpg)

    Firstly, the program obtains the player’s name and then greets the player.
    Secondly, the program asks the question “Would you like to play to play?” and takes input from the player to determine if the game continues or stops. If the player enters ‘n’, then the game is terminated. At the same time print out a goodbye message to the player. If the player enters ‘y’, then the game starts.
    The program displays rules after the input ‘y’ is identified and guides the player to make a move by entering 'r' for Rock, 'p' for Paper or 's' for Scissors.

    If the player wins, the computer displays a message and a partial image. Once the player has won 3 times, the computer displays a full image. Then the player is asked if they wish to replay the game or exit the game.

- **How to Play**

    The computer randomly chooses Rock, Paper or Scissors. The player can enter ‘r’ for Rock, ‘p’ for Paper or ‘s’ for Scissors to play against the computer. A player who decides to play rock will beat another player who has chosen scissors ("rock crushes scissors" or sometimes "blunts scissors"), but will lose to one who has played paper ("paper covers rock"); a play of paper will lose to a play of scissors ("scissors cuts paper"). If both players choose the same shape, the game is tied.
    If it’s a tie, the computer displays the following message:

    ![Tie](images/tie.jpg)

    If the player loses, the computer displays the following message:

    ![Player loses](images/lost.jpg)

    If the player wins, the computer displays a message and a partial image as below:

    ![Player wins](images/win.jpg)

    Once the player has won 3 time, the computer displays a full image as below:

    ![Full image](images/full_image.jpg)

    Then the player is asked if they wish to replay the game or exit the game.

[Back to the top](#overview)

### 3. **Testing and Launch**

- PEP8 validation

  - No errors or warnings were found when passing through the official PEP8 validator.

- Normal testing
  - The game runs smoothly with normal activities. Obtaining the player's name and capitalized the first letter correctly. Validating the player's input such as 'y' or 'n' for start or exit the game. Showing no issues for corrent moves as 'r', 'p' or 's', also image and message for tie, win or lost displayed accordingly. The game can be exited easily by enter 'n' and goodbye message displayed correctly. More details can be found as per following gif image.
  - ![testing-normal](images/testing-normal-30sec.gif)

- Function start() testing:
  - A bug was identified when testing on the start() function. There was a chance that a player may enter anything else other than y’ or ‘n. Hence used while…not in…: method to validate input and display a message to require the player to enter only ‘y’ or ‘n’ to start or exit the game. Then the player can exit the game by entering 'n' without any issue.
  - ![testing-input](images/input-validate.gif)

- Function play() testing:
  - The same bug fixed in play() function. The computer displays a message to the player if invalid input is identified. For example, the computer will display a message of "enter 'r' for Rock,'p' for Paper,'s' for Scissors" to the player if input identified as 'abc' where it should has been chosen 'r', 'p' or 's'.
  - ![testing input play function](images/input-validate-play-function.gif)

- Function player_win( ) testing:
  - The game is designed to allow the player to win 3 times of the game. However, there was a bug where the game ended after the player has won 2 times. It was fixed by updating the n value when called the function. It needed to be 5 other than 3 because of the math.ceiling method. 

- Goodbye message testing:
  - The game terminates if the player enters ‘n’  and  Goodbye message displayed as expected.
  - ![goodbye message](images/goodbye-message.gif)

- Technology Stack
  - [Python](https://www.python.org/)
  - [PEP8](http://pep8online.com/)
  - [Wiki](https://www.wikipedia.org/)
  - [Heroku]( https://dashboard.heroku.com/apps)
  - [Responsive design](http://ami.responsivedesign.is/#)
  - [Privacy Policy Generator](https://www.privacypolicygenerator.info/ )

[Back to the top](#overview)

### 4. **Deployment**

- The game was deployed to [Heroku]( https://dashboard.heroku.com/apps) page. The steps to deploy are as follows:

- In the Heroku page, select ‘Create new app’
![Heroku](images/Heroku.jpg)

- Create app name and choose a region

- Navigate to the setting tab. Add Python and node.js buildpacks
![buildpacks](images/buildpacks.png)

- At the deploy section, connect to Github, search and link to Rock-Paper-Scissors repository.
![buildpacks](images/github.jpg)

- Scroll down to set up automatic deploys, it enables Heroku to rebuild the app every time push code to Github.

- The live link can be found here [link]( https://rack-paper-scissors.herokuapp.com/)

[Back to the top](#overview)

### 5. **Support**

- Code Institute Tutor Assistance

  [Back to the top](#overview)

### 6. **Reference and Research**

- Reference
  - [Article 1](http://k.sina.com.cn/article_7059102645_p1a4c15bb500100hze9.html?from=cul )

[Back to the top](#overview)


