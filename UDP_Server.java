// import java.io.*; 
import java.net.*; 
public class UDP_Server 
{ 
 public static void main(String[] args) 
 { 
DatagramSocket skt=null; 
try 
{ 
System.out.println("server is started"); 
skt=new DatagramSocket(6788); 
byte[] buffer = new byte[1000]; 
while(true) 
{ 
DatagramPacket request = new DatagramPacket(buffer,buffer.length); 
skt.receive(request); 
String[] message = (new String(request.getData())).split(" "); 
byte[] sendMsg= (message[1].toUpperCase()+ " from server to client").getBytes(); 
DatagramPacket reply = new DatagramPacket(sendMsg,sendMsg.length,request.getAddress(),request.getPort()); 
skt.send(reply); 
} 
} 
catch(Exception ex) 
{ 
System.out.println(ex.getMessage()); 
} 
} 
} 