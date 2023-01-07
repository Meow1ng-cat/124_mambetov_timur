class Car{
    private String name;
    private String brand;
    private Integer year;
    private Integer total_distance;
    Car (String name, String brand, Integer year, Integer total_distance) {
        this.name = name;
        this.brand =  brand;
        this.year = year;
        this.total_distance = total_distance;
    }

    public void setName(String value){
        name = value;
    }
    public String  getName(){
        return name;
    }

    public void setBrand(String  value){brand = value;}
    public String getBrand(){
        return brand;
    }

    public void setYear(Integer value){ year = value;
        year = value;
    }
    public Integer getYear( ){
        return year;
    }

    public void setTotal_distance(Integer value){
        total_distance = value;
    }
    public Integer getTotal_distance( ){
        return total_distance;
    }

    public Integer trip(Integer value){
        this.total_distance = total_distance + value;
        return total_distance;
    }
}