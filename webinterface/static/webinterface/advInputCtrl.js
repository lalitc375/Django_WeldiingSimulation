  var app=angular.module('MyApp',[]);
  app.controller('AdvInputCtrl',function ($scope,$http){ //controller
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
  $scope.noXZone=3;
  $scope.noYZone=3;
  $scope.noZZone=1;
  $scope.pinLength=0;
  $scope.pinRadiusTip=0;
  $scope.pinRadiusRoot=0;
  $scope.shoulderRadius=5;
  $scope.threadPitch=5;
  $scope.threadPitch=0;
  //Advance Variable
  $scope.maxIteration=5000;
  $scope.underRelaxationUVelocity=0.6;
  $scope.underRelaxationVVelocity=0.6;
  $scope.underRelaxationWVelocity=0.6;
  $scope.underRelaxationPressure=0.6;
  $scope.underRelaxationTemp=0.7;
  $scope.heatCoffWest=100;
  $scope.heatCoffEast=100;
  $scope.heatCoffNorth=100;
  $scope.heatCoffSouth=100;
  $scope.heatCoffTop=0;
  $scope.heatCoffBottom=0.1;
  $scope.tempWest=298;
  $scope.tempEast=298;
  $scope.tempNorth=298;
  $scope.tempSouth=298;
  $scope.tempBottom=298;
  $scope.preHeatTemp=298;
  $scope.ambientTemp=298;
  $scope.fricCoff=0.4;
  $scope.slip=3;
  $scope.convFactMechHeat=0.8;
  $scope.adjViscousDiss=0.01;
  $scope.fracEnterWork=0.6;
//Dynamic Variable
  $scope.noXZone=3;
  $scope.noYZone=3;
  $scope.noZZone=1;
  $scope.noMonLoc=1;
  $scope.xShow=0;
  $scope.yShow=0;
  $scope.zShow=0;
  $scope.monLocShow=0;
  $scope.XLoc=[];
  $scope.XControl=[];
  $scope.XEpoCon=[];
  $scope.YLoc=[];
  $scope.YControl=[];
  $scope.YEpoCon=[];
  $scope.ZLoc=[];
  $scope.ZControl=[];
  $scope.ZEpoCon=[];

      $scope.XLoc.push({'value':7.0});
      $scope.XLoc.push({'value':3.0});
      $scope.XLoc.push({'value':7.0});
      $scope.XControl.push({'value':15});
      $scope.XControl.push({'value':120});
      $scope.XControl.push({'value':15});
      $scope.XEpoCon.push({'value':-1.2});
      $scope.XEpoCon.push({'value':1.0});
      $scope.XEpoCon.push({'value':1.2});
      $scope.YLoc.push({'value':7.0});
      $scope.YLoc.push({'value':3.0});
      $scope.YLoc.push({'value':7.0});
      $scope.YControl.push({'value':15});
      $scope.YControl.push({'value':120});
      $scope.YControl.push({'value':15});
      $scope.YEpoCon.push({'value':-1.3});
      $scope.YEpoCon.push({'value':1.0});
      $scope.YEpoCon.push({'value':1.3});
      $scope.ZLoc.push({'value':$scope.thicknessWorkpiece});
      $scope.ZControl.push({'value':15});
      $scope.ZEpoCon.push({'value':-1.3});

  $scope.createXVar=function(){
    $scope.xShow=1;
    $scope.XLoc=[];
    $scope.XControl=[];
    $scope.XEpoCon=[];
    if($scope.noXZone==3)
      {
      $scope.XLoc.push({'value':7.0});
      $scope.XLoc.push({'value':3.0});
      $scope.XLoc.push({'value':7.0});

      $scope.XControl.push({'value':15});
      $scope.XControl.push({'value':120});
      $scope.XControl.push({'value':15});

      $scope.XEpoCon.push({'value':-1.2});
      $scope.XEpoCon.push({'value':1.0});
      $scope.XEpoCon.push({'value':1.2});
      }
    else
    {
    for (var i = 0; i < $scope.noXZone; i++) {
      $scope.XLoc.push({'value':i});
      $scope.XEpoCon.push({'value':i});
      $scope.XControl.push({'value':i});
      };
    };  

  };
  

  $scope.createYVar=function(){
    $scope.YLoc=[];
    $scope.YControl=[];
    $scope.YEpoCon=[];
    $scope.yShow=1;
    if($scope.noYZone==3)
      {
      $scope.YLoc.push({'value':7.0});
      $scope.YLoc.push({'value':3.0});
      $scope.YLoc.push({'value':7.0});

      $scope.YControl.push({'value':15});
      $scope.YControl.push({'value':120});
      $scope.YControl.push({'value':15});
 
      $scope.YEpoCon.push({'value':-1.3});
      $scope.YEpoCon.push({'value':1.0});
      $scope.YEpoCon.push({'value':1.3});

      }
    else
    {
    for (var i = 0; i < $scope.noYZone; i++) {
      $scope.YLoc.push({'value':i});
      $scope.YEpoCon.push({'value':i});
      $scope.YControl.push({'value':i});
      };
    };
  };


  $scope.createZVar=function(){
    $scope.zShow=1;
    $scope.ZLoc=[];
    $scope.ZControl=[];
    $scope.ZEpoCon=[];
    if($scope.noZZone==1)
      {
      $scope.ZLoc.push({'value':$scope.thicknessWorkpiece});
      $scope.ZControl.push({'value':15});
      $scope.ZEpoCon.push({'value':-1.3});

      }
    else
    {
    for (var i = 0; i < $scope.noZZone; i++) {
      $scope.ZLoc.push({'value':i});
      $scope.ZEpoCon.push({'value':i});
      $scope.ZControl.push({'value':i});
      };
      };
   }; 
  
  $scope.createMonLoc=function(){
    $scope.monYLoc=[];
    $scope.monZLoc=[];
    $scope.monLocShow=1;
    
    for (var i = 0; i < $scope.noMonLoc; i++) {
      $scope.monZLoc.push({'value':i});
      $scope.monYLoc.push({'value':i});
     
      };
    };
    $scope.msg="";
    $scope.clearall=function()
    {
      $scope.advancingMaterial="";
      $scope.toolRpm="";
      $scope.pinLength="";
      $scope.pinRadiusTip="";
      $scope.pinRadiusRoot="";
      $scope.noXZone=1;
      $scope.noYZone=1;
      $scope.tiltAngle="";
      $scope.toolRpm="";
      $scope.threadPitch="";
      $scope.XLoc=[];
      $scope.YLoc=[];
      $scope.ZLoc=[];
      $scope.XControl=[];
      $scope.XEpoCon=[];
      $scope.YControl=[];
      $scope.YEpoCon=[];
      $scope.ZControl=[];
      $scope.ZEpoCon=[];


      $scope.shoulderRadius="";
      $scope.toolMaterial="";
      $scope.feedRate="";
      $scope.axialPressure="";
      $scope.thicknessWorkpiece="";
      $scope.yLocTool="";
      $scope.xLocTool="";
    };
  $scope.input=function(){
	if($scope.advancingMaterial.value!="" && $scope.toolMaterial.value!=""&&$scope.threadPitch!=""&&$scope.thicknessWorkpiece!="" && $scope.shoulderRadius!="" && $scope.pinRadiusRoot!="" && $scope.pinRadiusTip!="" && $scope.pinLength!="" && $scope.feedRate!="" && $scope.toolRpm!="" && $scope.axialPressure!="" && $scope.tiltAngle!="" && $scope.noXZone!="" && $scope.noYZone!="")
 		{
 			var XLocString="";
      var XControlString="";
      var XEpoConString="";
      for (var i = 0; i < $scope.noXZone; i++) {
        XLocString+=String($scope.XLoc[i].value)+"@";
        XControlString+=String($scope.XControl[i].value)+"@";
        XEpoConString+=String($scope.XEpoCon[i].value)+"@";
      };
      var YLocString="";
      var YControlString="";
      var YEpoConString="";
      for (var i = 0; i < $scope.noYZone; i++) {
        YLocString+=String($scope.YLoc[i].value)+"@";
        YControlString+=String($scope.YControl[i].value)+"@";
        YEpoConString+=String($scope.YEpoCon[i].value)+"@";
      };
      var ZLocString="";
      var ZControlString="";
      var ZEpoConString="";
      for (var i = 0; i < $scope.noZZone; i++) {
        ZLocString+=String($scope.ZLoc[i].value)+"@";
        ZControlString+=String($scope.ZControl[i].value)+"@";
        ZEpoConString+=String($scope.ZEpoCon[i].value)+"@";
      };
      var monYLocString="";
      var monZLocString="";
      for (var i = 0; i < $scope.noMonLoc; i++) {
        monYLocString+=String($scope.monYLoc[i].value)+"@";
        monZLocString+=String($scope.monZLoc[i].value)+"@";       
      };
      if($scope.noZZone==1)
        ZLocString=String($scope.thicknessWorkpiece)+"@";			
 			var inputData={
 				"advancingMaterial":$scope.advancingMaterial.value,
        "retreatingMaterial":$scope.retreatingMaterial.value,
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
        "noYZone":$scope.noYZone,
        "noXZone":$scope.noXZone,
        "noZZone":$scope.noZZone, 
        "XLocString":XLocString,
        "XControlString":XControlString,
        "XEpoConString":XEpoConString,
        "YLocString":YLocString,
        "YControlString":YControlString,
        "YEpoConString":YEpoConString,
        "ZLocString":ZLocString,
        "ZControlString":ZControlString,
        "ZEpoConString":ZEpoConString,
        "noMonLoc":$scope.noMonLoc,
        "monYLocString":monYLocString,
        "monZLocString":monZLocString,
        "maxIteration":$scope.maxIteration,
        "underRelaxationTemp":$scope.underRelaxationTemp,
        "underRelaxationPressure":$scope.underRelaxationPressure,
        "underRelaxationUVelocity":$scope.underRelaxationUVelocity,
        "underRelaxationWVelocity":$scope.underRelaxationWVelocity,
        "underRelaxationVVelocity":$scope.underRelaxationVVelocity,
        "tempBottom":$scope.tempBottom,
        "tempSouth":$scope.tempSouth,
        "tempNorth":$scope.tempNorth,
        "tempEast":$scope.tempEast,
        "tempWest":$scope.tempWest,
        "heatCoffBottom":$scope.heatCoffBottom,
        "heatCoffTop":$scope.heatCoffTop,
        "heatCoffSouth":$scope.heatCoffSouth,
        "heatCoffEast":$scope.heatCoffEast,
        "heatCoffWest":$scope.heatCoffWest,
        "heatCoffNorth":$scope.heatCoffNorth,
        "fricCoff":$scope.fricCoff,
        "slip":$scope.slip,
        "fracEnterWork":$scope.fracEnterWork,
        "convFactMechHeat":$scope.convFactMechHeat,
        "fracEnterWork":$scope.fracEnterWork,
        "preHeatTemp":$scope.preHeatTemp,
        "ambientTemp":$scope.ambientTemp,
        "adjViscousDiss":$scope.adjViscousDiss

    
 			};

 	



 			$http.post("bin/feedAdvUserData.php",inputData)
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