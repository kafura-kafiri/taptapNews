 
 app.controller('AdminController', ['$scope', function($scope) {
        $scope.sendNews = function(id,title,date,image,source,tags,breif) {
            alert(source);
            };
        $scope.sendTagInfo = function(name,oldname,del) {
            alert(del);
            };
        $scope.block = function(username) {
            alert(username);
            };
        }
]);
