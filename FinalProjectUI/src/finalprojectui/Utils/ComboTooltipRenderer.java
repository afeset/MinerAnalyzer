/*
 * To change this template, choose Tools | Templates
 * and open the template in the editor.
 */
package finalprojectui.Utils;

import java.awt.Component;
import javax.swing.DefaultListCellRenderer;
import javax.swing.JComponent;
import javax.swing.JList;

/**
 *
 * @author dell
 */
public class ComboTooltipRenderer extends DefaultListCellRenderer {

    public Component getListCellRendererComponent(JList list, Object
    value, int index, boolean isSelected,
    boolean cellHasFocus)
    {
        JComponent comp = (JComponent)super.getListCellRendererComponent(list, value, index, isSelected, cellHasFocus);
        if (value != null) 
        {
            comp.setToolTipText(String.valueOf(value));
        } 
        else 
        {
            comp.setToolTipText(null);
        }
        return comp;
    }
}
