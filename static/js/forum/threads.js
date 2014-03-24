BaseApp.controller("ForumThreadCtrl", function($scope, $http){
    //On controller load
    var forum_thread = this;
    forum_thread.dupe = false;
    forum_thread.posting = false;
    forum_thread.new_thread = {};
    forum_thread.incomplete = {'name': false, 'message': false};

    //functions
    forum_thread.createThread = function(){
        if(!forum_thread.new_thread.name){
            forum_thread.incomplete.name = true;
            return;
        }
        else if(!forum_thread.new_thread.message){
            forum_thread.incomplete.name = false;
            forum_thread.incomplete.message = true;
            return;
        }
        else{
            forum_thread.incomplete.name = false;
            forum_thread.incomplete.message = false;
            forum_thread.posting = true;
            $http.post(window.location.pathname, forum_thread.new_thread)
            .success(function(response){
                if(response == 'dupe'){
                    forum_thread.dupe = true;
                    forum_thread.incomplete.name = true;
                    forum_thread.posting = false;
                }
                else{
                    window.location = response;
                }
            });
        }
    };
});
                
