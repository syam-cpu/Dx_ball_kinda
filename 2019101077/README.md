Introduction:
	This is a famous game called DX-BALL.The Player plays by moving the paddle back and forth.Player should aim to not to miss the Ball and let it touch the ground.There will be a Brick layout on hitting the Brick with Ball Player can increase his score.Player will have certain number of lives and he trys to maximise his score with those lives.In middle of the game Player will very randomly encounter some things falling from Bricks place after destroying it ,called powerups.Player can catch them with paddle.Once cacthed they will change the characteristics of the objects present.They will exist only for a certain time. After that player will get his elements in initial state (before picking powerups)


                            E - Expands Paddle
                            S - Shrinks Paddle
                            M - Ball multiplier
                            F - Fast Ball
                            T - Thru Ball
			    G - Paddle Grab


Game Play:
       At first you will launch the ball
       Next you will control the paddle in such a way that you will get ball on it 
       The Ball will go and hit the Bricks ,walls and gets reflected.
       When you hit brick color transition of kind R->G->B happens
       You can increase your score by hitting the Breakable bits
       Your Game ends when your lives get exhausted

Controls:

       a - Moves the Paddle Left
       d - Moves the Paddle Right
       Space-Bar - Launces the Ball
       q - Quits the game
        

The Classes:
       
    Board
         Board class encapsulates the all Display functionality.It contains the methods for rendering various elements and cleaning Screen.It prints the every element of screen the way we want.

     
    Paddle
        Paddle class contains all the functionality related to paddle movements and shape.It contains methods for moving Paddle ,setting the type of paddle and getting various attributes of paddle

    Ball
        Ball class encapsulates all the functionality related to ball movements and shape .It contains methods for moving Ball,changing the velocity of ball and getting various attributes of Ball.It also
        contains the methods for checking collision with Brick and Paddle.

    Brick
        It encapsulates all the functionality related to Brick.It contains very shapes of bricks ,type,strength of bricks.It contains methods for setting and getting various attributes of Bricks.

    Power_up
         It encapsulates the all the power_up functionality.It contains methods for returning shapes,moving powerups,getting type of power_ups,getting state of powerups and so on.
        


Oops Concepts:

    Inheritance:
         Brick1 ,Brick2,Brick3,Brick4 all these classes inherit from Brick class

    Polymorphism:
        All methods present in Parent class Power_up are overridden in the child classes Power_up1 ,Power_up2,Power_up3,Power_up4,Power_up5,Power_up6

    Encapsulation:
        Through out the game it contains class and objects that encapsulate different entities

    
    Abstraction:
        Methods like Ball.check_ collsion_with_paddle(),Ball.check_collsion_Brick() ,Ball.move() ,Board.print_grid(),Board.Place_in_grid() abstracts away the details and makes code more readable.
