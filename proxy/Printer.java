public class Printer implements IPrinter{

    ColorPrinter ColorP;
    SWPrinter SWP;
    String currentPrinter;

    public Printer(){
        this.currentPrinter = "SW";
        this.ColorP = new ColorPrinter();
        this.SWP = new SWPrinter();
    }

    @Override
    public void print(String text) {
        if (this.currentPrinter.equals("SW")){
            this.SWP.print(text);
        }else {
            this.ColorP.print(text);
        }
    }

    public void changePrinter(String s){
        if (s.toUpperCase().equals(this.currentPrinter)){
            System.out.println("Already selected!");
        }else if(s.toUpperCase().equals("SW")){
            currentPrinter = "SW";
        }else if (s.toUpperCase().equals("COLOR")){
            currentPrinter = "COLOR";
        }else{
            System.out.println("No valid choice!");
        }
    }
}