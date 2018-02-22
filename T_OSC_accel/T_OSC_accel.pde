import oscP5.*;
import netP5.*;

OscP5 oscP5;


//for Accelerometer values
float degreeX = 0; 
float degreeZ = 0;   
float tdegreeX = 0;   
float tdegreeZ = 0;
float transX = 0; 
float ttransX = 0;

float curX = 0;
float curY = 0;
float curZ = 0;
float preX = 0;
float preY = 0;
float preZ = 0;
boolean isGetFirst = false;


void setup() {
    size(400, 400, P3D);

    oscP5 = new OscP5(this, 12000);

    oscP5.plug(this, "accxyz", "/accxyz");
    
    ttransX = width/2;
}


void draw() {
    background(38, 41, 44);

    //update rotate degree on x-axis and z-axis
    degreeX = degreeX + (tdegreeX-degreeX)/30;
    degreeZ = degreeZ + (tdegreeZ-degreeZ)/30;

    //update shift location on x-axis
    transX = transX + (ttransX-transX)/30;
    
    pushMatrix();
    translate(transX, height/2);
    rotateX(radians(degreeX));
    rotateZ(radians(degreeZ));
    drawSimplePhone();
    popMatrix();
}

void drawSimplePhone(){
    strokeWeight(1);
    stroke(0);
    fill(255);
    box(65, 10, 140);

    strokeWeight(3);
    stroke(255, 0, 0);
    line(0, -10, -30, 0, -10, -80);
    line(0, -10, -80, -10, -10, -60);
    line(0, -10, -80, 10, -10, -60);
}


public void accxyz(float x, float y, float z) {
//    println("recieved (x, y, z) = (" + x + ", " + y + ", " + z + ")" ); 

    if(!isGetFirst){
        curX = x;
        curY = y;
        curZ = z;
        isGetFirst = true;
    }else{
        preX = curX;
        preY = curY;
        preZ = curZ;
        curX = x;
        curY = y;
        curZ = z;
    }

    if(dist(curX, curY, curZ, preX, preY, preZ) < 1){
        return; 
    }


    tdegreeX = constrain(y*-9, -90, 90); 

    transX = ttransX + x*-9;  
    
    if(abs(tdegreeX) < 80){   
        tdegreeZ = constrain(z*9 - 90, -180, 0); 
    }else{
        tdegreeZ = z*9;
    }
}


/* incoming osc message are forwarded to the oscEvent method. */
void oscEvent(OscMessage theOscMessage) {

    //check unknow OSC message from touchOSC app    
    if (theOscMessage.isPlugged()==false) {
        /* print the address pattern and the typetag of the received OscMessage */
        println("### received an osc message.");
        println("### addrpattern\t"+theOscMessage.addrPattern());
        println("### typetag\t"+theOscMessage.typetag());
    }
}