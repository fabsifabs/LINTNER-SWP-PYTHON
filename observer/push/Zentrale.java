package push;
import java.util.ArrayList;

public class Zentrale{

    private ArrayList<Anzeige> anzeigen;

    public Zentrale(){
        this.anzeigen = new ArrayList<Anzeige>();
    }


    public void addAnzeige(Anzeige a){
        this.anzeigen.add(a);
    }

    public void delAnzeige(Anzeige a){
        this.anzeigen.remove(a);
    }


    public void sendData(String s){
        for (Anzeige anzeige : anzeigen) {
            anzeige.getData(s);
        }
    }

}