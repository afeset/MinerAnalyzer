/*
 * To change this template, choose Tools | Templates
 * and open the template in the editor.
 */
package finalprojectui.Reports.UserAgentStatisticsReport;

import finalprojectui.Entities.Pair;
import java.awt.BorderLayout;
import java.awt.Dimension;
import java.util.List;
import java.util.Vector;
import javax.swing.JScrollPane;
import javax.swing.JTable;
import javax.swing.table.DefaultTableModel;
import javax.swing.table.TableModel;
import org.jfree.chart.ChartFactory;
import org.jfree.chart.ChartPanel;
import org.jfree.chart.JFreeChart;
import org.jfree.chart.axis.CategoryAxis;
import org.jfree.chart.axis.CategoryLabelPositions;
import org.jfree.chart.axis.NumberAxis;
import org.jfree.chart.axis.ValueAxis;
import org.jfree.chart.labels.ItemLabelAnchor;
import org.jfree.chart.labels.ItemLabelPosition;
import org.jfree.chart.labels.StandardCategoryItemLabelGenerator;
import org.jfree.chart.plot.CategoryPlot;
import org.jfree.chart.plot.PiePlot3D;
import org.jfree.chart.plot.PlotOrientation;
import org.jfree.chart.renderer.category.BarRenderer;
import org.jfree.chart.renderer.category.StackedBarRenderer;
import org.jfree.data.category.CategoryDataset;
import org.jfree.data.category.DefaultCategoryDataset;
import org.jfree.data.general.DefaultPieDataset;
import org.jfree.data.general.PieDataset;
import org.jfree.ui.TextAnchor;
import org.jfree.util.Rotation;

/**
 *
 * @author dell
 */
public class UserAgentStatisticsReportReaultsPanel extends javax.swing.JPanel {
    private double _NumberOfTransactionsResult;
   private double _NumberOfBytesResult;
    /**
     * Creates new form
     * RequestsPercentagePerHeaderReportParametersPanelReaultsPanel
     */
    public UserAgentStatisticsReportReaultsPanel() {
        initComponents();
        this.setLayout(new BorderLayout());
    }
    
    public void loadLists()
    {
        UserAgentStatisticsReportLoader loader=new UserAgentStatisticsReportLoader(null);
        loader.load();
        _NumberOfTransactionsResult=loader.getNumberOfTransactionsResult();
        _NumberOfBytesResult=loader.getNumberOfBytesResult();
    }
    public void loadTable()
    {
        JTable resTable=new JTable();
        loadLists();
        
        String[] columnNames={"","% Transactions", "% Bytes"};
        DefaultTableModel model=new DefaultTableModel(columnNames,1);
        model.setValueAt("Problematic user agents", 0, 0);
        model.setValueAt(_NumberOfTransactionsResult, 0, 1);
        model.setValueAt(_NumberOfBytesResult, 0, 2);
        
        resTable.setModel(model);
        JScrollPane scrollPane = new JScrollPane(resTable);
        this.removeAll();
        this.add(scrollPane, BorderLayout.CENTER);
        this.revalidate();
    }
    
    public void loadGraph()
    {
        loadLists();        
        
        CategoryDataset dataset = createDataset();
        JFreeChart chart = createChart(dataset);
        ChartPanel chartPanel = new ChartPanel(chart);
        chartPanel.setPreferredSize(new Dimension(500, 270));
        this.removeAll();
        this.add(chartPanel, BorderLayout.CENTER);
        this.revalidate();
        
    }
    
    /**
     * Returns a sample dataset.
     * 
     * @return The dataset.
     */
    private CategoryDataset createDataset() {
        
        // row keys...
        String transSeries = "% Transactions";
        String bytesSeries = "% Bytes";
        
        DefaultCategoryDataset dataset = new DefaultCategoryDataset();
        
        dataset.addValue(_NumberOfTransactionsResult, transSeries, "");
        dataset.addValue(_NumberOfBytesResult, bytesSeries, "");
        
        return dataset;
        
    }
    
    private JFreeChart createChart(final CategoryDataset dataset) {
        
        // create the chart...
        final JFreeChart chart = ChartFactory.createBarChart(
            "User Agent Statistics Report",         // chart title
            "Problematic user agents",               // domain axis label
            "Percentage",                  // range axis label
            dataset,                  // data
            PlotOrientation.VERTICAL, // orientation
            true,                     // include legend
            true,                     // tooltips?
            false                     // URLs?
        );

        // NOW DO SOME OPTIONAL CUSTOMISATION OF THE CHART...

        // set the background color for the chart...
        //chart.setBackgroundPaint(Color.white);

        // get a reference to the plot for further customisation...
        CategoryPlot plot = chart.getCategoryPlot();
        
        //plot.setBackgroundPaint(Color.lightGray);
        //plot.setDomainGridlinePaint(Color.white);
        //plot.setRangeGridlinePaint(Color.white);

        // set the range axis to display integers only...
        NumberAxis rangeAxis = (NumberAxis) plot.getRangeAxis();
        rangeAxis.setStandardTickUnits(NumberAxis.createIntegerTickUnits());
        ValueAxis axis = plot.getRangeAxis();
        //axis.setRange(0, 100);
        
        //set values to show on bars
        BarRenderer renderer = (BarRenderer) plot.getRenderer();
        renderer.setBaseItemLabelsVisible(true);
        renderer.setBaseItemLabelGenerator(new StandardCategoryItemLabelGenerator());
        renderer.setDrawBarOutline(false);
        renderer.setBasePositiveItemLabelPosition(new ItemLabelPosition(ItemLabelAnchor.OUTSIDE12,TextAnchor.TOP_CENTER));
        renderer.setItemMargin(0.2);
        renderer.setMaximumBarWidth(0.1);
        

        return chart;
        
    }
    

    
    
 

    /**
     * This method is called from within the constructor to initialize the form.
     * WARNING: Do NOT modify this code. The content of this method is always
     * regenerated by the Form Editor.
     */
    @SuppressWarnings("unchecked")
    // <editor-fold defaultstate="collapsed" desc="Generated Code">//GEN-BEGIN:initComponents
    private void initComponents() {

        javax.swing.GroupLayout layout = new javax.swing.GroupLayout(this);
        this.setLayout(layout);
        layout.setHorizontalGroup(
            layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
            .addGap(0, 400, Short.MAX_VALUE)
        );
        layout.setVerticalGroup(
            layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
            .addGap(0, 300, Short.MAX_VALUE)
        );
    }// </editor-fold>//GEN-END:initComponents
    // Variables declaration - do not modify//GEN-BEGIN:variables
    // End of variables declaration//GEN-END:variables
}
