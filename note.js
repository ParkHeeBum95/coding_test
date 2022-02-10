
function Rect(width, height) {
    this.width = width;
    this.height = height;
    this.getarea = function (){
    return this.width * this.height;
    };
    }
}

const rect1 = new Rect(3,4);
const rect2 = new Rect(5,6);



