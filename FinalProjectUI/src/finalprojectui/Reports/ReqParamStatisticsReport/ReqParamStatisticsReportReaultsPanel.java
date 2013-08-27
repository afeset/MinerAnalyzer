/*
 * To change this template, choose Tools | Templates
 * and open the template in the editor.
 */
package finalprojectui.Reports.ReqParamStatisticsReport;

import finalprojectui.Entities.Pair;
import java.awt.*;
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
import org.jfree.chart.plot.PiePlot;
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
public class ReqParamStatisticsReportReaultsPanel extends javax.swing.JPanel {
    private double _requestsWithURIParamTrans;
    private double _requestsWithoutURIParamTrans;
    
    private double _requestsWithURIParamBytes;
    private double _requestsWithoutURIParamBytes;
    
    private double _requestsWithParamEqZeroTrans;
    private double _requestsWithParamEqZeroBytes;
    
    private double _requestsWithParamNotEqZeroTrans;
    private double _requestsWithParamNotEqZeroBytes;
    
    /**
     * Creates new form
     * RequestsPercentagePerHeaderReportParametersPanelReaultsPanel
     */
    public ReqParamStatisticsReportReaultsPanel() {
        initComponents();
        this.setLayout(new GridBagLayout());
        
    }
    
    public void loadGraph()
    {
        loadData();
        this.removeAll();   
        
        GridBagConstraints c = new GridBagConstraints();
        c.fill = GridBagConstraints.BOTH;
        c.ipadx=this.getWidth()/2;
        c.ipady=this.getHeight()/2;
        JFreeChart transPieChart=getTransPieChart();
        ChartPanel transChartPanel = new ChartPanel(transPieChart);
        c.fill = GridBagConstraints.BOTH;
        c.gridx = 0;
        c.gridy = 0;
        this.add(transChartPanel, c);
        
        JFreeChart bytesPieChart=getBytesPieChart();
        ChartPanel bytesChartPanel = new ChartPanel(bytesPieChart);
        c.fill = GridBagConstraints.BOTH;
       // c.weightx = 0.5;
        c.ipadx=this.getWidth()/2;
        c.ipady=this.getHeight()/2;
        c.gridx = 1;
        c.gridy = 0;
        this.add(bytesChartPanel, c);
        
        JFreeChart eqaulZeroChart=getEqaulZeroChart();
        ChartPanel equalZeroChartPanel = new ChartPanel(eqaulZeroChart);
        c.fill = GridBagConstraints.BOTH;
        //c.ipady = 40;      //make this component tall
      //  c.weightx = 0.0;
        c.ipadx=this.getWidth();
        c.ipady=this.getHeight()/2;
        c.gridwidth = 3;
        c.gridx = 0;
        c.gridy = 1;
        
        this.add(equalZeroChartPanel, c);
        
        this.revalidate();
    }
    
    public void loadTable()
    {
        loadData();
        JTable resTable=new JTable();
        
        String[] columnNames={"","% Transactions", "% Bytes"};
        DefaultTableModel model=new DefaultTableModel(columnNames,4);
        
        model.setValueAt("Requests with URI param", 0, 0);
        model.setValueAt(_requestsWithURIParamTrans, 0, 1);
        model.setValueAt(_requestsWithURIParamBytes, 0, 2);
        
        model.setValueAt("Requests without URI param", 1, 0);
        model.setValueAt(_requestsWithoutURIParamTrans, 1, 1);
        model.setValueAt(_requestsWithoutURIParamBytes, 1, 2);
        
        model.setValueAt("Requests with param = 0", 2, 0);
        model.setValueAt(_requestsWithParamEqZeroTrans, 2, 1);
        model.setValueAt(_requestsWithParamEqZeroBytes, 2, 2);
        
        model.setValueAt("Requests with param <> 0", 3, 0);
        model.setValueAt(_requestsWithParamNotEqZeroTrans, 3, 1);
        model.setValueAt(_requestsWithParamNotEqZeroBytes, 3, 2);
        
        
        resTable.setModel(model);
        JScrollPane scrollPane = new JScrollPane(resTable);
        this.removeAll();
        GridBagConstraints c = new GridBagConstraints();
        c.fill = GridBagConstraints.BOTH;
        c.ipadx=this.getWidth();
        c.ipady=this.getHeight();
        c.gridx = 0;
        c.gridy = 0;
        this.add(scrollPane, c);
        this.revalidate();

    }
    
    public void loadData()
    {
        ReqParamStatisticsReportLoader loader=new ReqParamStatisticsReportLoader(null);
        loader.load();
        
        _requestsWithParamEqZeroBytes=loader.getRequestsWithParamEqZeroBytes();
        _requestsWithParamEqZeroTrans=loader.getRequestsWithParamEqZeroTrans();
        _requestsWithParamNotEqZeroBytes=loader.getRequestsWithParamNotEqZeroBytes();
        _requestsWithParamNotEqZeroTrans=loader.getRequestsWithParamNotEqZeroTrans();
        _requestsWithURIParamBytes=loader.getRequestsWithURIParamBytes();
        _requestsWithURIParamTrans=loader.getRequestsWithURIParamTrans();
        _requestsWithoutURIParamBytes=loader.getRequestsWithoutURIParamBytes();
        _requestsWithoutURIParamTrans=loader.getRequestsWithoutURIParamTrans();
          
    }
    
    private JFreeChart getTransPieChart()
    {
        DefaultPieDataset dataset = new DefaultPieDataset();
        dataset.setValue("With URI Param 'begin'", new Double(_requestsWithURIParamTrans));
        dataset.setValue("Without URI Param 'begin'", new Double(_requestsWithoutURIParamTrans));
        
        JFreeChart chart = ChartFactory.createPieChart(
            "% Transactions - URI Param 'begin'",  // chart title
            dataset,             // data
            true,               // include legend
            true,
            false
        );

        PiePlot plot = (PiePlot) chart.getPlot();
        plot.setLabelFont(new Font("SansSerif", Font.PLAIN, 12));
        plot.setNoDataMessage("No data available");
        plot.setCircular(false);
        plot.setLabelGap(0.02);
        
        return chart;
    }
    
    private JFreeChart getBytesPieChart()
    {
        DefaultPieDataset dataset = new DefaultPieDataset();
        dataset.setValue("With URI Param 'begin'", new Double(_requestsWithURIParamBytes));
        dataset.setValue("Without URI Param 'begin'", new Double(_requestsWithoutURIParamBytes));
        
        JFreeChart chart = ChartFactory.createPieChart(
            "% Bytes - URI Param 'begin'",  // chart title
            dataset,             // data
            true,               // include legend
            true,
            false
        );

        PiePlot plot = (PiePlot) chart.getPlot();
        plot.setLabelFont(new Font("SansSerif", Font.PLAIN, 12));
        plot.setNoDataMessage("No data available");
        plot.setCircular(false);
        plot.setLabelGap(0.02);
        
        return chart;
    }
    
    
    private JFreeChart getEqaulZeroChart() {
        
        // row keys...
        String eqaultZero = "Begin = 0";
        String notEqualZero = "Begin <> 0";
        String transSeries = "% Transactions";
        String bytesSeries = "% Bytes";
        
        
        DefaultCategoryDataset dataset = new DefaultCategoryDataset();
        // column keys...
        dataset.addValue(_requestsWithParamEqZeroTrans, transSeries, eqaultZero);
        dataset.addValue(_requestsWithParamEqZeroBytes, bytesSeries, eqaultZero);

        dataset.addValue(_requestsWithParamNotEqZeroTrans, transSeries, notEqualZero);
        dataset.addValue(_requestsWithParamNotEqZeroBytes, bytesSeries, notEqualZero);
        
        // create the chart...
        final JFreeChart chart = ChartFactory.createBarChart(
            "Begin Param=0 / Begin param<>0",         // chart title
            "",               // domain axis label
            "Percentage",                  // range axis label
            dataset,                  // data
            PlotOrientation.VERTICAL, // orientation
            true,                     // include legend
            true,                     // tooltips?
            false                     // URLs?
        );

        // get a reference to the plot for further customisation...
        CategoryPlot plot = chart.getCategoryPlot();
        
        // set the range axis to display integers only...
        NumberAxis rangeAxis = (NumberAxis) plot.getRangeAxis();
        rangeAxis.setStandardTickUnits(NumberAxis.createIntegerTickUnits());
        ValueAxis axis = plot.getRangeAxis();
        
        //set values to show on bars
        BarRenderer renderer = (BarRenderer) plot.getRenderer();
        renderer.setBaseItemLabelsVisible(true);
        renderer.setBaseItemLabelGenerator(new StandardCategoryItemLabelGenerator());
        renderer.setDrawBarOutline(false);
        renderer.setBasePositiveItemLabelPosition(new ItemLabelPosition(ItemLabelAnchor.OUTSIDE12,TextAnchor.TOP_CENTER));
        renderer.setItemMargin(0);
        
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
