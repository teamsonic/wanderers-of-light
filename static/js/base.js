var BaseApp = angular.module("Base", []);


BaseApp.controller("FooterCtrl", function($scope){
    //Executed on Controller load
    var footer = this;
    this.hidden = true;

    //functions
    this.slide = function(){
        var elem = $("div.footer-content");
        if(this.hidden){
            elem.animate({'height': 200}, {'duration': 500, 'easing': 'swing'});
            this.hidden = false;
        }
        else{
            elem.animate({'height': 0}, {'duration': 500, 'easing': 'swing'});
            this.hidden = true;
        }
    };

    this.isHidden = function(){
        if(this.hidden){
            return "glyphicon-chevron-up";
        }
        else{
            return "glyphicon-chevron-down";
        }
    };

});
