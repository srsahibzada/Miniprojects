/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 * tutorial starts at http://www.edu4java.com/en/game/game1.html ; edu4java minitennis game tutorial
 */
package simplegame;

import javax.swing.JFrame;
import java.awt.Color;
import java.awt.Graphics;
import java.awt.Graphics2D;
import java.awt.RenderingHints;
import java.awt.geom.Ellipse2D;
import javax.swing.JFrame;
import javax.swing.JPanel;
import java.awt.event.KeyEvent;
import java.awt.event.KeyListener;
import javax.swing.JOptionPane;
import java.awt.Rectangle;
/**
 *
 * @author srsahibzada
 */
//simple key listener class


class Racquet{
int x = 0;
int xv = 0;
private static final int y = 350;
private static final int width = 80;
private static final int height = 20;

private Simplegame sg;

public Racquet(Simplegame sim){
    this.sg = sim;
};

public void moveRacquet(){
/*    if (x + xv < 0) xv = 1;
    if (x + xv > (sg.getWidth() - 40)) xv = -1;*/
    if (x + xv > 0 && x + xv < sg.getWidth()- 80) x = x + xv;
    //if we're moving to the right AND not yet at the end
    
    //x = x + xv; //set x
}

public void paint(Graphics2D g){
    g.fillRect(x,y,width,height);
}

public void keyReleased(KeyEvent e){
    xv = 0;
}

public void keyPressed(KeyEvent e){
    if (e.getKeyCode() == KeyEvent.VK_LEFT) xv = -2; //move to the left
    if (e.getKeyCode() == KeyEvent.VK_RIGHT) xv = 2; //move to the right
}

public Rectangle getBounds(){
    return new Rectangle(x,y,width,height);
}

public int get_top_y(){
    return y;
}

}


class Ball{
    int x = 0;
    int y = 0;
    int xv = 1; //manipulate x direction
    int yv = 1; //manipulate y direction
    private final int diam = 40;
    private Simplegame sg; //reference the simplegame panel
    
    public Ball(Simplegame sim){
        this.sg = sim;
    }
    
   // int xv = 0;
   // int yv = 0;
    public void moveBall(){
       if (x + xv < 0) xv = 1; //if you're too far left, move right
       if (x + xv > (sg.getWidth() - diam)) xv = -1;
       //so if you are at the far right, move left.
       if (y + yv < 0) yv = 1; //too far up, move down
       if (y + yv > (sg.getHeight() - diam)) sg.gameOver();  //too far down, move up
       if (collides()){
           //change direction
           yv = -1;
           //set the new position of y to the top of the racquet
           y = sg.r.get_top_y() - diam;
       }
      
       //moves the ball up if you are at the end 
        x = x+xv;
        y = y+yv;
    }
    
    public void paint(Graphics2D g){
        g.fillOval(x,y,diam,diam);
    }
    
    public Rectangle getBounds(){
        return new Rectangle(x,y,diam,diam);
    }
    
    private boolean collides(){
        if (sg.r.getBounds().intersects(this.getBounds()))
                return true;
        else return false;
    }
}
public class Simplegame extends JPanel{
   // public Simplegame(){}
   
    Ball b = new Ball(this);
    Racquet r = new Racquet(this);

   // @Override 
   // public void paint(Graphics g){
      /*  Graphics2D gg = (Graphics2D) g;
        gg.setColor(Color.GREEN);
        gg.fillOval(0,0,30,30); //makes a filled oval at these points
        gg.drawOval(0,50,30,30); //makes a nonfilled oval at these points
        gg.fillRect(50,0,30,30);
        gg.drawRect(50,50,30,30);
        
        gg.draw(new Ellipse2D.Double(0,100,30,30));*/
        
    //make a constructor that uses an anonymous class to register some key listener
      public Simplegame(){ 
           addKeyListener(new KeyListener() {
   
          
            @Override
            public void keyTyped(KeyEvent e){
            }
            
            @Override
            public void keyPressed(KeyEvent e){
               System.out.println("keyPressed="+KeyEvent.getKeyText(e.getKeyCode()));
                 r.keyPressed(e);
            }
            
            @Override
            public void keyReleased(KeyEvent e){
              System.out.println("Key released." + KeyEvent.getKeyText(e.getKeyCode()));
                r.keyReleased(e);
            }
  
        });
         setFocusable(true);
      }
    
   // KeyListener kl = new KeyListener();
    
    private void move(){
        b.moveBall();
        r.moveRacquet();
    }
    public void gameOver(){
        JOptionPane j = new JOptionPane();
        j.showMessageDialog(this, "Game Over", "Game Over!s", JOptionPane.YES_NO_OPTION);
        System.exit(ABORT);
    }
    @Override
    public void paint(Graphics g){
        super.paint(g);
        Graphics2D g2d = (Graphics2D) g;
        g2d.setRenderingHint(RenderingHints.KEY_ANTIALIASING, RenderingHints.VALUE_ANTIALIAS_ON);
        b.paint(g2d);
        r.paint(g2d);
    }
    
    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) throws InterruptedException{
     try {
      
       
       JFrame frame = new JFrame("Sarah's Game");
       //KeyboardAction k = new KeyboardAction();
       Simplegame g = new Simplegame();
       //frame.addKeyListener(keylist);
       frame.add(g);
       //frame.add(k);
       frame.setSize(400,400);
       frame.setVisible(true);
       frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
      while (true) {
			g.move();
			g.repaint();
			Thread.sleep(10);
		}
    }
   
    catch(InterruptedException ie){
    System.out.println("exception occurred");
}
    
}
}
