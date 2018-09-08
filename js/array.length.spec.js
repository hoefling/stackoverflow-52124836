var assert = require('assert');

describe('Array', function() {
  describe('#length', function() {
    it('should be 0 when the array is empty', function() {
      assert.equal([].length, 0);
    });
    it('should be 1 when the array has one element', function() {
      assert.equal([null].length, 1);
    });
    it('should be 2 when the array has two elements', function() {
      assert.equal([null, null].length, 2);
    });
  });
});
