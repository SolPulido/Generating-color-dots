from browser import document, html, window, alert 
import random 

def sketch (p): # This P is needed  because is a parameter it will be the processing sketch itself 
  # To do things like background color. 
  # background (0) instead  of p.background(0)
  def setup(): 
    p.createCanvas(1900,1000)
    p.background(255)
    p.rectMode (p.CENTER)
  def draw():
    colorlist =['red','pink','black','gray']
    p.noStroke()
    p.fill(random.choice(colorlist))
    p.ellipse(p.mouseX,p.mouseY,50,50)
  def mousePressed(self):
    p.background(0)
  def keyPressed(self):
    if p.key ==" ":
      print("Space pressed!")
  p.setup = setup 
  p.draw = draw
  p.mousePressed = mousePressed
  p.keyPressed = keyPressed

myp5=window.p5.new(sketch)


  