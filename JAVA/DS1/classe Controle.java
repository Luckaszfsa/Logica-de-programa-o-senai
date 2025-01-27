public class Controle {
    
    
    private int canal;
    private int volume;

    public Controle(int canal, int volume) {
        this.canal = canal;
        this.volume = volume;
    }

    public int getCanal() {
        return canal;
    }

    public void setCanal(int canal) {
        if (canal >=0 && canal<= 100){
        this.canal = canal;
    }
    }
        

    public int getVolume() {
        return volume;
    }

    public void setVolume(int volume) {
        this.volume = volume;
    }
    
    public void aumentarVolume() {
        if (this.volume < 100){
            this.volume+= 1;
        }
    
}
    public void diminuirVolume() {
        if (this.volume >0){
            this.volume -= 1;
    }
    }
    
    public static void main(String[] args) {
        Controle controle = new Controle(10,15);
        System.out.println(controle.canal);
        System.out.println(controle.volume);
        controle.aumentarVolume();
        controle.setCanal(50);
        for(int i = 0; i<10; i++){
            controle.aumentarVolume();
        }
        System.out.println(controle.canal);
        System.out.println(controle.volume);
    }
}
