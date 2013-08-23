/*
 * To change this template, choose Tools | Templates
 * and open the template in the editor.
 */
package finalprojectui.Entities;

/**
 *
 * @author dell
 */
public class Pair<K,V> {
    private K key;
    private V value;
    public Pair(K k, V v){
        this.key = k;
        this.value = v;
    }
    public K getKey(){ return key; }
    public V getValue(){ return value; }
    public void setL(K k){ this.key = k; }
    public void setR(V v){ this.value = v; }
}
