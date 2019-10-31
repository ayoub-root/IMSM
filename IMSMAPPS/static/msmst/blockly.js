class Component {
constructor(name){
    this.name=name;
}}
////////////////////////
class Device {
constructor(name){
    this.name=name;
}}
 //alert("ffff  ")
            function device(name,bg,description) {

  Blockly.Blocks[name] = {
  init: function() {

    this.appendDummyInput()
        .setAlign(Blockly.ALIGN_RIGHT)
        .appendField(new Blockly.FieldImage(bg, 115, 115, { alt: "*", flipRtl: "FALSE" }));
    this.appendStatementInput("NAME")
        .setCheck(null);
    this.setPreviousStatement(true, null);
    this.setNextStatement(true, null);
    this.setColour(230);
 this.setTooltip(description);
 this.setHelpUrl("");
  }
};
Blockly.JavaScript[name] = function(block) {
 return 'new Device("'+name+'");'+'\n';
};
Blockly.Python[name] = function(block) {
  return 'device_("'+name+'")\n';
};
}
        function component(name,bg,description) {

  Blockly.Blocks[name] = {

  init: function() {
    this.appendDummyInput()
        .setAlign(Blockly.ALIGN_CENTRE)
        .appendField(new Blockly.FieldImage(bg, 115, 115, { alt: "*", flipRtl: "TRUE"}));
    this.appendStatementInput("NAME")
        .setCheck(null);
    this.setPreviousStatement(false, null);
    this.setNextStatement(true, null);
    this.setColour(230);
 this.setTooltip(description);
 this.setHelpUrl("");
  }
};
Blockly.JavaScript[name] = function(block) {
     var text = Blockly.JavaScript.statementToCode(block, 'NAME',
      Blockly.JavaScript.ORDER_MEMBER) || '\'\'';
 return 'new Component("'+name+'");'+'\n'+"{ "+text+" }";
};
Blockly.Python[name] = function(block) {
  return 'component_("'+name+'")\n';
};
}          //    alert("{{ post.name }}");
  function microservice(name) {

Blockly.Blocks[name] = {
  init: function() {
    this.appendValueInput("NAME")
        .setAlign(Blockly.ALIGN_CENTRE)
        .appendField(name);
    this.setInputsInline(false);
    this.setPreviousStatement(true, null);
    this.setNextStatement(true, null);
    this.setColour(230);
 this.setTooltip("");
 this.setHelpUrl("");
  }
};



}
  function data(name) {

  Blockly.Blocks[name] = {
  init: function() {
    this.appendStatementInput("NAME")
        .setCheck(null);

    this.setPreviousStatement(false, null);
    this.setNextStatement(false, null);
    this.setColour(230);
 this.setTooltip("");
 this.setHelpUrl("");
  }
};

}