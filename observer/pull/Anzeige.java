package pull;
public abstract class Anzeige{

    private String data = "";
    public Anzeige(){
    }

    public void getNotified(){
        System.out.println("there is new Data");
    }

    public void setData(String s){
        this.data = s;
    }

    public String getData(){
        return this.data;
    }
}