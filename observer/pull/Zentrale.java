package pull;
import java.util.ArrayList;

public class Zentrale{

    private ArrayList<Anzeige> anzeigen;
    private String currentData = ""; 

    public Zentrale(){
        this.anzeigen = new ArrayList<Anzeige>();
    }


    public void addAnzeige(Anzeige a){
        this.anzeigen.add(a);
    }

    public void delAnzeige(Anzeige a){
        this.anzeigen.remove(a);
    }

    public void setCurrentData(String s){
        this.currentData = s;
        notif();
    }

    public void notif(){
        for (Anzeige anzeige : anzeigen) {
            anzeige.getNotified();
        }
    }

    public String returnData(){
        return currentData;
    }

}