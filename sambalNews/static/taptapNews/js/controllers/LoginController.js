

 app.controller('LoginController', ['$scope', function($scope, $http) {
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
            }

            $http.post('http://localhost:8000/sambalNews/login', data, config)
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