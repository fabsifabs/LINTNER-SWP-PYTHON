package push;

public class main{
    public static void main (String[] args){

        Zentrale z = new Zentrale();
        
        Anzeige pool = new poolAnzeige();
        Anzeige haus = new hausAnzeige();
        
        z.addAnzeige(pool);
        z.addAnzeige(haus);
        z.sendData("newData");
        z.delAnzeige(haus);
        z.sendData("otherData");

    } 
}