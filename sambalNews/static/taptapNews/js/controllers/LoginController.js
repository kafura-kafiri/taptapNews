

 app.controller('LoginController', ['$scope','$http', function($scope,$http) {
          $scope.login = function (username,password) {
            var data = $.param(
                {
                    data: {
                        username: username,
                        password: password
                    }
                }
            );

            var config = {
                headers : {
                    'Content-Type': 'application/x-www-form-urlencoded;charset=utf-8;'
                }
            };

              $http.post('/sambalNews/login/', data, config)
                .success(function (data, status, headers, config) {
                    if(data.length>50){
                        $scope.ResponseDetails = "http://127.0.0.1:8000/sambalNews/index";
                    }
                    else
                        $scope.ResponseDetails = data;
            })
            .error(function (data, status, header, config) {
                $scope.ResponseDetails = "Data: " + data +
                    "<hr />status: " + status +
                    "<hr />headers: " + header +
                    "<hr />config: " + config;
            });
        };
     $scope.signUp = function (username,password,email) {
            var data = $.param(
                {
                    data: {
                        username: username,
                        password: password,
                        email: email
                    }
                }
            );

            var config = {
                headers : {
                    'Content-Type': 'application/x-www-form-urlencoded;charset=utf-8;'
                }
            }

              $http.post('/sambalNews/signup', data, config)
                .success(function (data, status, headers, config) {
                    $scope.ResponseDetails = data;
            })
            .error(function (data, status, header, config) {
                $scope.ResponseDetails = "Data: " + data +
                    "<hr />status: " + status +
                    "<hr />headers: " + header +
                    "<hr />config: " + config;
            });
        };
        }
]);