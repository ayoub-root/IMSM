Code.workspace.clear();

// alert("fffff");
function new_block(name, argss, cmd_run, path, conin, conout, type, description) {
    // alert(type+""+name);
    //   var code = '{"name":'+name+',"cmd_run":'+cmd_run+',"args":,"path":'+path+',"type":'+type+'}';
  //  alert("ssss");
 var args= [];
 var msg="";

 var t=JSON.parse($("<div/>").html(argss).text());




 for (var i in t){
    // alert('"'+t[i]+'"');
    args.push({"type":"input_value","name":'"'+t[i]+'"',"align": "RIGHT"});
     msg+= t[i]+"%"+(+i+1)+" ";
 }
//alert(msg);
//alert(args[2].name);
    var data = {
        "message0": name +"   " + msg,
        "args0":args
    }
    Blockly.Blocks[name] = {
        init: function () {

            this.jsonInit(data);
            this.setPreviousStatement(conin, null);
            this.setNextStatement(conout, null);

            this.setColour(230);
            this.setTooltip(description);
            this.setHelpUrl("");
        }
    };
/*
    Blockly.JavaScript[name] = function (block) {
     var val=[] ; var value_args=[];
    for (j in t){
        var p="'"+t[j]+"'";
        alert(p)
     value_args[j]   = Blockly.JavaScript.valueToCode(block, p, Blockly.JavaScript.ORDER_ATOMIC);
        // TODO: Assemble JavaScript into code variable.


           val[j] =  block.getFieldValue(p);

    }
 alert(val[0]+"  ss  "+value_args[0]);
        var code = "run_ms("+val[1]+")\n";
        //alert("aaaa"+value);
       return  code;
    };*/


Blockly.JavaScript[name] = function(block) {
    var val=[];
    for (i in t){
     //   alert('"'+t[i]+'"');
          val[i] = Blockly.JavaScript.valueToCode(block, '"'+t[i]+'"', Blockly.JavaScript.ORDER_ATOMIC);
    }

 return 'jsmicroservice__("'+name+'",' + val + ');\n';
};

   Blockly.Python[name] = function(block) {
    var val=[];
    for (i in t){
     //   alert('"'+t[i]+'"');
          val[i] = Blockly.Python.valueToCode(block, '"'+t[i]+'"', Blockly.Python.ORDER_ATOMIC);
    }

  return 'self.pymicroservice__("'+name+'",' + val + ');\n';
};
}

function loadWorkspace(xml_text) {
Code.workspace.clear();
    var xml = Blockly.Xml.textToDom(xml_text);

 //  alert( xml_text)
    Blockly.Xml.domToWorkspace(xml, Code.workspace);
  }

  function save() {
   // alert('ssss')
      var xml = Blockly.Xml.workspaceToDom(Code.workspace);
        var xml_text = Blockly.Xml.domToText(xml);
       // alert(xml_text);
   //var xml = Blockly.Xml.workspaceToDom(Blockly.getMainWorkspace());
$.post("/save_app",{'app_name':$("#app").val(),'app_code':xml_text.replace(/"/g, '\\"')},function (data) {
//alert(data)
});
//

  }
