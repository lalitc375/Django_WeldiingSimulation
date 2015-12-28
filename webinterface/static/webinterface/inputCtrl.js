  var app=angular.module('MyApp',[]);
  app.controller('InputCtrl',function ($scope,$http){ //controller
  $scope.advancingMaterials=[{name:"A",value:1}
  ,{name:"B",value:2}
  ,{name:"C",value:3}
  ,{name:"D",value:4}
  ,{name:"E",value:5}
  ,{name:"F",value:6}];

  $scope.retreatingMaterials=[{name:"A",value:1}
  ,{name:"B",value:2}
  ,{name:"C",value:3}
  ,{name:"D",value:4}
  ,{name:"E",value:5}
  ,{name:"F",value:6}];

  $scope.toolMaterials=[{name:"A",value:1}
  ,{name:"B",value:2}
  ,{name:"C",value:3}
  ,{name:"D",value:4}
  ,{name:"E",value:5}
  ,{name:"F",value:6}];

 
  $scope.noMonLoc=1;
  $scope.monLocShow=0;
  
  $scope.createMonLoc=function(){
    $scope.monYLoc=[];
    $scope.monZLoc=[];
    $scope.monLocShow=1;
    
    for (var i = 0; i < $scope.noMonLoc; i++) {
      $scope.monZLoc.push({'value':i});
      $scope.monYLoc.push({'value':i});
     
    };
      };
  $scope.clearall=function()
    {
      $scope.advancingMaterial="";
      $scope.toolRpm="";
      $scope.pinLength="";
      $scope.pinRadiusTip="";
      $scope.pinRadiusRoot="";
     
      $scope.tiltAngle="";
      $scope.toolRpm="";
      $scope.threadPitch="";
     
      $scope.shoulderRadius="";
      $scope.toolMaterial="";
      $scope.feedRate="";
      $scope.axialPressure="";
      $scope.thicknessWorkpiece="";
      $scope.yLocTool="";
      $scope.xLocTool="";


    };

  
  $scope.msg="";
  $scope.input=function(){
	if($scope.advancingMaterial.value!="" && $scope.toolMaterial.value!=""&&$scope.threadPitch!=""&&$scope.thicknessWorkpiece!="" && $scope.shoulderRadius!="" && $scope.pinRadiusRoot!="" && $scope.pinRadiusTip!="" && $scope.pinLength!="" && $scope.feedRate!="" && $scope.toolRpm!="" && $scope.axialPressure!="" && $scope.tiltAngle!="" && $scope.noXZone!="" && $scope.noYZone!="")
 		{
 			
      var monYLocString="";
      var monZLocString="";
      for (var i = 0; i < $scope.noMonLoc; i++) {
        monYLocString+=String($scope.monYLoc[i].value)+"@";
        monZLocString+=String($scope.monZLoc[i].value)+"@";       
      };
 			$scope.thicknessWorkpiece=String($scope.thicknessWorkpiece)+"@";

 			
 			var inputData={
 				"advancingMaterial":$scope.advancingMaterial.value,
 				"toolMaterial":$scope.toolMaterial.value,
 				"thicknessWorkpiece":$scope.thicknessWorkpiece,
 				"feedRate":$scope.feedRate,
 				"shoulderRadius":$scope.shoulderRadius,
 				"pinRadiusRoot":$scope.pinRadiusRoot,
 				"pinRadiusTip":$scope.pinRadiusTip,
 				"pinLength":$scope.pinLength,
 				"toolRpm":$scope.toolRpm,
 				"axialPressure":$scope.axialPressure,
 				"tiltAngle":$scope.tiltAngle,
 				"threadPitch":$scope.threadPitch,
        "xLocTool":$scope.xLocTool,
        "yLocTool":$scope.yLocTool,
        "noMonLoc":$scope.noMonLoc,
        "monYLocString":monYLocString,
        "monZLocString":monZLocString
        
 			};
 			$http.post("bin/feedUserData.php",inputData)
 			.success(function(data,status){
 				$scope.status=angular.fromJson(data); 
 				if($scope.status.submitStatus==1)
 					{
					
					$scope.clearall();
					window.location.href="bin/submission.php";
 					$scope.msg="Your Data for Processing is Accepted.Soon You will recieve Mail";				
 					}
 				else if($scope.status.submitStatus==3)
 					{
 					$scope.msg="All Field r Mandatory";
 					}

 			}).error(function(){
 					$scope.msg="Please Try After Some Time";
 			}); 		
 		}
 	else
 	$scope.msg="All Field Are Mandatory";
 	
 	
 	};
 


});