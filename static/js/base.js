var BaseApp = angular.module("Base", []);


BaseApp.controller("FooterCtrl", function($scope){
    //Executed on Controller load
    var footer = this;
    footer.hidden = true;

    //functions
    footer.slide = function(){
        var elem = $("div.footer-content");
        if(footer.hidden){
            elem.animate({'height': 200}, {'duration': 500, 'easing': 'swing'});
            footer.hidden = false;
        }
        else{
            elem.animate({'height': 0}, {'duration': 500, 'easing': 'swing'});
            footer.hidden = true;
        }
    };

    footer.isHidden = function(){
        if(footer.hidden){
            return "glyphicon-chevron-up";
        }
        else{
            return "glyphicon-chevron-down";
        }
    };

});
