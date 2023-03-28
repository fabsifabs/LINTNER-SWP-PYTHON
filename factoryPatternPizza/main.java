public class main{

    public static void main(String[] args){
        Pizzeria NY = new PizzariaNY(){};
        Pizza piz = NY.pizzamachen("salami");
        piz.backen();
    }
}