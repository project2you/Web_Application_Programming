// Listing 2.2: ตัวอย่าง React Component ที่สร้างจาก V0.dev
// หัวข้อ: 2.3.3 V0.dev: การสร้าง UI จาก Text Prompt
import React, { useState } from 'react';
import { BarChart3, TrendingUp, Download, Settings } from 'lucide-react';

// Card Components
const Card = ({ className = "", children, ...props }) => (
  <div 
    className={`rounded-lg border border-white/20 bg-white/10 backdrop-blur-lg shadow-lg ${className}`}
    {...props}
  >
    {children}
  </div>
);

const CardHeader = ({ className = "", children, ...props }) => (
  <div className={`flex flex-col space-y-1.5 p-6 ${className}`} {...props}>
    {children}
  </div>
);

const CardTitle = ({ className = "", children, ...props }) => (
  <h3 
    className={`text-2xl font-semibold leading-none tracking-tight text-white ${className}`}
    {...props}
  >
    {children}
  </h3>
);

const CardDescription = ({ className = "", children, ...props }) => (
  <p className={`text-sm text-gray-300 ${className}`} {...props}>
    {children}
  </p>
);

const CardContent = ({ className = "", children, ...props }) => (
  <div className={`p-6 pt-0 ${className}`} {...props}>
    {children}
  </div>
);

const CardFooter = ({ className = "", children, ...props }) => (
  <div className={`flex items-center p-6 pt-0 ${className}`} {...props}>
    {children}
  </div>
);

// Button Component
const Button = ({ 
  variant = "default", 
  className = "", 
  children, 
  ...props 
}) => {
  const baseStyles = "inline-flex items-center justify-center rounded-md text-sm font-medium transition-colors focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-white disabled:pointer-events-none disabled:opacity-50 px-4 py-2";
  
  const variants = {
    default: "bg-blue-600 text-white hover:bg-blue-700",
    outline: "border border-white/30 bg-transparent hover:bg-white/10 text-white",
    ghost: "hover:bg-white/10 text-white"
  };
  
  return (
    <button 
      className={`${baseStyles} ${variants[variant]} ${className}`}
      {...props}
    >
      {children}
    </button>
  );
};

// Simple Chart Component
const SimpleChart = ({ data }) => {
  const maxValue = Math.max(...data.map(d => d.value));
  
  return (
    <div className="flex items-end justify-between h-full gap-2">
      {data.map((item, index) => (
        <div key={index} className="flex flex-col items-center flex-1 gap-2">
          <div className="w-full bg-white/10 rounded-t-md relative" style={{ height: '100%' }}>
            <div 
              className="absolute bottom-0 w-full bg-gradient-to-t from-blue-500 to-blue-400 rounded-t-md transition-all duration-500 hover:from-blue-400 hover:to-blue-300"
              style={{ height: `${(item.value / maxValue) * 100}%` }}
            />
          </div>
          <span className="text-xs text-gray-400">{item.label}</span>
        </div>
      ))}
    </div>
  );
};

// Main Dashboard Card Component
export default function DashboardCard() {
  const [isExpanded, setIsExpanded] = useState(false);
  
  // Sample data
  const chartData = [
    { label: 'Mon', value: 45 },
    { label: 'Tue', value: 62 },
    { label: 'Wed', value: 38 },
    { label: 'Thu', value: 75 },
    { label: 'Fri', value: 55 },
    { label: 'Sat', value: 48 },
    { label: 'Sun', value: 30 }
  ];
  
  const metrics = [
    { label: 'Total Users', value: '12,543', change: '+12.5%', positive: true },
    { label: 'Revenue', value: '$45,231', change: '+8.2%', positive: true },
    { label: 'Bounce Rate', value: '32.4%', change: '-5.3%', positive: true },
    { label: 'Avg. Session', value: '4m 23s', change: '+15.7%', positive: true }
  ];

  return (
    <div className="min-h-screen bg-gradient-to-br from-slate-900 via-purple-900 to-slate-900 p-8 flex items-center justify-center">
      <div className="w-full max-w-4xl">
        <Card className="w-full">
          <CardHeader>
            <div className="flex items-center justify-between">
              <div className="flex items-center gap-3">
                <div className="p-2 bg-blue-500/20 rounded-lg">
                  <BarChart3 className="w-6 h-6 text-blue-400" />
                </div>
                <div>
                  <CardTitle className="flex items-center gap-2">
                    Analytics Overview
                    <TrendingUp className="w-5 h-5 text-green-400" />
                  </CardTitle>
                  <CardDescription>
                    Last 30 days performance metrics
                  </CardDescription>
                </div>
              </div>
              <Button variant="ghost" className="rounded-full w-10 h-10 p-0">
                <Settings className="w-5 h-5" />
              </Button>
            </div>
          </CardHeader>
          
          <CardContent>
            {/* Metrics Grid */}
            <div className="grid grid-cols-2 md:grid-cols-4 gap-4 mb-6">
              {metrics.map((metric, index) => (
                <div 
                  key={index}
                  className="p-4 rounded-lg bg-white/5 border border-white/10 hover:bg-white/10 transition-colors"
                >
                  <p className="text-xs text-gray-400 mb-1">{metric.label}</p>
                  <p className="text-2xl font-bold text-white mb-1">{metric.value}</p>
                  <p className={`text-xs flex items-center gap-1 ${metric.positive ? 'text-green-400' : 'text-red-400'}`}>
                    <TrendingUp className="w-3 h-3" />
                    {metric.change}
                  </p>
                </div>
              ))}
            </div>
            
            {/* Chart Area */}
            <div className="h-[240px] flex items-center justify-center rounded-lg bg-white/5 border border-white/10 p-4">
              <SimpleChart data={chartData} />
            </div>
            
            {/* Additional Info (Expandable) */}
            {isExpanded && (
              <div className="mt-4 p-4 rounded-lg bg-white/5 border border-white/10 animate-in fade-in slide-in-from-top-2 duration-300">
                <h4 className="text-sm font-semibold text-white mb-2">Detailed Insights</h4>
                <ul className="space-y-2 text-sm text-gray-300">
                  <li>• Peak traffic hours: 2PM - 5PM</li>
                  <li>• Top performing page: /products</li>
                  <li>• Mobile users: 68% of total traffic</li>
                  <li>• Average conversion rate: 3.2%</li>
                </ul>
              </div>
            )}
          </CardContent>
          
          <CardFooter className="flex gap-2">
            <Button variant="default" className="flex-1">
              <Download className="w-4 h-4 mr-2" />
              Export Data
            </Button>
            <Button 
              variant="outline" 
              className="flex-1"
              onClick={() => setIsExpanded(!isExpanded)}
            >
              {isExpanded ? 'Hide' : 'View'} Details
            </Button>
          </CardFooter>
        </Card>
      </div>
    </div>
  );
}
