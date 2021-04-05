// Setup
var collection = {
  2548: {
    albumTitle: 'Slippery When Wet',
    artist: 'Bon Jovi',
    tracks: ['Let It Rock', 'You Give Love a Bad Name']
  },
  2468: {
    albumTitle: '1999',
    artist: 'Prince',
    tracks: ['1999', 'Little Red Corvette']
  },
  1245: {
    artist: 'Robert Palmer',
    tracks: []
  },
  5439: {
    albumTitle: 'ABBA Gold'
  }
};

// Only change code below this line
function updateRecords(object, id, prop, value) {
  if (value == '') {
    delete object[id][prop]
  } else {
      switch (prop) {
      case 'albumTitle':
      case 'artist':
        object[id][prop] = value
        break;
      case 'tracks':
        if (object[id].hasOwnProperty(prop) === false) {
          object[id][prop] = [value]
        } else {
          object[id][prop].push(value)
        }
        break;
      }
    }
  
  return object;
}

console.log(updateRecords(collection, 5439, "tracks", "Take a Chance on Me"));