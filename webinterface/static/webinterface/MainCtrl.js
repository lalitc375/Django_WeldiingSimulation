 var mainApp=angular.module('mainApp', ['ngRoute']);
 angular.element(document.getElementsByTagName('head')).append(angular.element('<base href="' + window.location.pathname + '" />'));
 
 mainApp.config(['$routeProvider', '$locationProvider',
 	function($routeProvider, $locationProvider) {
 		$routeProvider
 		.when('/', {
 			templateUrl: 'templates/login.html',
 			controller: 'loginCtrl',
 		})
 		.when('/login', {
 			templateUrl: 'templates/login.html',
 			controller: 'loginCtrl',
 		})
 		.when('/signup', {
 			templateUrl: 'templates/signup.html',
 			controller: 'signupCtrl',
 		})
 		.when('/input',{
 			templateUrl:'templates/input.html',
 			controller:'inputCtrl',
 		})
 	}]);
 mainApp.controller('MainCtrl', function($scope,$http) {
 });
 mainApp.controller('signupCtrl', function($scope,$http) {
 	$scope.branchs=["Biomedical",
 	"Biotech",
 	"Chemical",
 	"Civil",
 	"Computer Science",
 	"Electrical",
 	"Electronics and telecommunication",
 	"Information Technology",
 	"Mechanical",
 	"Metallurgy",
 	"Mining"
 	];
 	$scope.branch="Biotech";
 	$scope.passmatch=0;
 	$scope.checkpass=function(){
 		if($scope.password===$scope.cpassword)
 			$scope.passmatch=1;
 		else
 			$scope.passmatch=2;
 	};
 	$scope.clearall=function(){
 		$scope.email="";
 		$scope.address="";
 		$scope.company="";
 		$scope.name="";
 		$scope.contact="";
 		$scope.profession="";
 		$scope.password="";
 		$scope.cpassword="";
 		$scope.passmatch=0;
 	}
 	$scope.type1="Basic";
 	$scope.types=["Basic","Advance"];
 	$scope.signup=function(){
 		if($scope.email!="" && $scope.name!="" && $scope.contact!="" && $scope.password!="" && $scope.passmatch==1&& $scope.profession!="" &&$scope.designation!="" && $scope.company!="" && $scope.address!=""&&$scope.type1!="")
 		{
 			var user={
 				"email":$scope.email,
 				"name":$scope.name,
 				"ph_no":$scope.contact,
 				"profession":$scope.profession,
 				"designation":$scope.designation,
 				"password":$scope.password,
 				"company":$scope.company,
 				"address":$scope.address,
 				"type1":$scope.type1

 			};
 			$http.post("bin/signup.php",user)
 			.success(function(data,status){
 				$scope.status=angular.fromJson(data); 
 				if($scope.status.signupstatus==1)
 					{
 					$scope.clearall();
 					}
 					alert($scope.status.msg);

 			}).error(function(){
 				alert("error");
 			});
 		}
 	};
 });
 mainApp.controller('loginCtrl', function($scope,$http,$location) {
 	$scope.email="";
 	$scope.password="";
 	
 	$scope.check=function()
 	{
 		$http.post("bin/check.php",{})
 			.success(function(data,status){
 				$scope.status=angular.fromJson(data);
 				//alert($scope.status.loginstatus);
 				if($scope.status.loginstatus==0)
 					window.location.href="input.php";
 				else if($scope.status.loginstatus==1)
 					window.location.href="advanceinput.php";


 			}).error(function(){alert("error");})
 	};
 	$scope.check();
 	$scope.login=function(){
 		if($scope.email!="" && $scope.password!="")
 		{
 			$http.post("bin/login.php",{"email":$scope.email,"password":$scope.password})
 			.success(function(data,status){
 				$scope.status=angular.fromJson(data);
 				if($scope.status.loginstatus==0)
 					window.location.href="input.php";
 				else if($scope.status.loginstatus==1)
 					window.location.href="advanceinput.php";
 				else if($scope.status.loginstatus==2)
 					alert("Admin Approval Pending");
 				else if($scope.status.loginstatus==3)
 					alert("incorrect UserName or password");
 				//alert($scope.status.loginstatus);


 				});
 			}
 		};

 	});
