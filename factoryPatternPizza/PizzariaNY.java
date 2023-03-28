

public class PizzariaNY extends Pizzeria {
    public PizzariaNY(){}

    public Pizza pizzamachen(String sorte){
        Pizza piz  = new Pizza() {};
        if (sorte.equals("salami")){
            piz = new SalamiNY();
        }
        return piz;

    }
}
