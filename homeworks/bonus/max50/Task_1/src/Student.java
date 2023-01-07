class Student{
    private String name;
    private Integer age;
    private String group;
    private Double mean_score;
    Student(String name, Integer age, String group, Double mean_score) {
        this.name = name;
        this.age =  age;
        this.group = group;
        this.mean_score = mean_score;
    }

    public void setName(String value){
        name = value;
    }
    public String  getName(){
        return name;
    }

    public void setAge(Integer value){age = value;}
    public Integer getAge(){
        return age;
    }

    public void setGroup(String value){ group = value;
        group = value;
    }
    public String getGroup( ){
        return group;
    }

    public void setMean_score(Double value){
        mean_score = value;
    }
    public Double getMean_score( ){
        return mean_score;
    }
}