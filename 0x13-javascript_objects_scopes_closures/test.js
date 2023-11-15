#!/usr/bin/node

function Course (title, instructor, level, views){
  this.title = title;
  this.instructor = instructor;
  this.level = level;
  this.views = views;
  this.updateviews = function (){
    return ++this.views;
  };
};

var course1 = new Course("JSET", "Silicon", 1, 10);
var course2 = new Course("PET", "Alaska", 2, 40);
var cou = [course1, course2];
console.log(cou[1].instructor);
//console.log(course1);
//console.log(course2);
//console.log(course1.updateviews());