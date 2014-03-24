BaseApp.controller("ForumMessagesCtrl", function($scope, $http){
    //executed on controller load
    var forum_msg = this;    
    forum_msg.new_msg = '';
    forum_msg.posting = false;
    forum_msg.incomplete = false;

    //functions
    forum_msg.postMessage = function(){
        if(!forum_msg.new_msg.length){
            forum_msg.incomplete = true;
            return;
        }
        else{
            forum_msg._postMessage();
        }
    }; 

    forum_msg._postMessage = function(){
        forum_msg.posting = true;
        path = window.location.pathname;
        $http.post(path, {'message': forum_msg.new_msg})
        .success(function(response){
            window.location.reload();
        });
    };

});
