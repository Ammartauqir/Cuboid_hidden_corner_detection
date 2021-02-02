# Cuboid_hidden_corner_detection
<!-- TABLE OF CONTENTS -->
<details open="open">
  <summary><h2 style="display: inline-block">Table of Contents</h2></summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#Required-libraries">Required Libraries</a></li>
      </ul>
    </li>
    <li>
      <a href="#annotation">Annotation</a>
    </li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgements">Acknowledgements</a></li>
  </ol>
</details>


<!-- ABOUT THE PROJECT -->
## About The Project
The project is aimed to compute the position of the hidden corner of a cuboid in an image. The program takes the following as inputs:
* Image of the Cuboid
* Coordinates (x,y) of the 7 visble corners of the cuboid

The program will give the following outputs:

* Position of the hidden edges and hidden corner
* Uncertainity assosiated with the computed hidden corner

<!-- REQUIRED LIBRARIES -->
### Required Libraries

* OpenCV
* Numpy

## Usage 
The program takes path of an image as an input argument. The visible corners can then manually be selected using the mouses-coursor. `main.py` file envokes the program and path of the image is given after `-i`. A folder is included that contains some test images. 
_For Example_
```sh
python main.py -i pictures/pics2/box2.png
   ```
After the image has been loaded, an annotation window appears. The window allows you to annotate the visible corners of the displayed cuboid using `double-click` of the mouse-coursor. "Annotation rules" must be considered when annotating the Seven Visible corners.

## Annotation Rules
<img src="pictures/readme1.png" >
