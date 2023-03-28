package pull;

public class main{
    public static void main (String[] args){

        Zentrale z = new Zentrale();
        
        Anzeige pool = new poolAnzeige();
        Anzeige haus = new hausAnzeige();
        
        z.addAnzeige(pool);
        z.addAnzeige(haus);
        z.setCurrentData("thisData");
        
        pool.setData(z.returnData());
        System.out.println(pool.getData());
        
        /*
        z.delAnzeige(haus);
        z.setCurrentData("otherData");
        pool.setData(z.returnData());
        System.out.println(pool.getData());
        */
    } 
}