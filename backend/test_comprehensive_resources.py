#!/usr/bin/env python3
"""
Comprehensive Quality Resource Test
Tests the enhanced resource system to ensure many high-quality resources per subskill
"""
import sys
sys.path.append('.')

from utils.resource_search import get_resources_for_skill
from utils.enhanced_uniqueness import (
    ensure_resource_uniqueness_and_quality, 
    get_specialized_resources_for_subskill,
    get_performance_metrics,
    validate_url_accessibility
)

def test_comprehensive_resources():
    print("🎯 COMPREHENSIVE QUALITY RESOURCE TEST")
    print("=" * 80)
    print("Testing enhanced system for MANY high-quality resources per subskill")
    print()
    
    # Test with specific DSA subskills
    subskills = ["Arrays", "Linked Lists", "Binary Trees", "Stacks", "Dynamic Programming"]
    all_resources = []
    
    for i, subskill in enumerate(subskills, 1):
        print(f"📚 SUBSKILL {i}: {subskill}")
        print("-" * 60)
        
        # Get specialized resources (hand-curated)
        specialized = get_specialized_resources_for_subskill(subskill)
        print(f"✨ Specialized Resources: {len(specialized)}")
        
        # Get additional resources with increased parameters
        general = get_resources_for_skill(subskill, max_per_type=4)
        print(f"🔍 Additional Resources: {len(general)}")
        
        # Combine and ensure uniqueness & quality
        combined_resources = specialized + general
        unique_resources = ensure_resource_uniqueness_and_quality(
            combined_resources, subskill, max_resources=8  # Increased for comprehensive coverage
        )
        
        print(f"✅ FINAL RESOURCES: {len(unique_resources)} unique, validated resources")
        print()
        
        # Analyze resource diversity
        resource_types = {}
        quality_scores = []
        
        for j, resource in enumerate(unique_resources, 1):
            title = resource.get('title', 'No title')
            url = resource.get('url', '')
            quality = resource.get('quality_score', 0)
            resource_type = resource.get('resource_type', 'unknown')
            
            # Count resource types
            resource_types[resource_type] = resource_types.get(resource_type, 0) + 1
            quality_scores.append(quality)
            
            print(f"  {j:2d}. {title[:70]}")
            print(f"      Type: {resource_type.ljust(12)} | Quality: {quality:3.0f}/100")
            print(f"      URL: {url}")
            
            # Quick validation check
            # is_valid = validate_url_accessibility(url)
            # status = "✅ VALID" if is_valid else "❌ INVALID"
            # print(f"      Status: {status}")
            print()
        
        # Display diversity analysis
        print("📊 RESOURCE ANALYSIS:")
        print(f"   🎭 Types: {list(resource_types.keys())}")
        print(f"   📋 Type Counts: {resource_types}")
        avg_quality = sum(quality_scores) / len(quality_scores) if quality_scores else 0
        print(f"   ⭐ Average Quality: {avg_quality:.1f}/100")
        print(f"   🌈 Type Diversity: {len(resource_types)} different types")
        print()
        
        all_resources.extend(unique_resources)
        print(f"📊 CUMULATIVE TOTAL: {len(all_resources)} resources")
        print("=" * 80)
        print()
    
    # Overall analysis
    print("🎯 OVERALL PERFORMANCE ANALYSIS")
    print("=" * 80)
    
    performance = get_performance_metrics(all_resources)
    
    print(f"📈 Performance Grade: {performance['performance_grade']}")
    print(f"📊 Overall Score: {performance['overall_score']}/100")
    print(f"🔗 Total Resources: {performance['total_resources']}")
    print(f"⭐ Average Quality Score: {performance['avg_quality_score']}/100")
    print(f"🎭 Uniqueness Score: {performance['uniqueness_score']}%")
    print(f"🌈 Resource Diversity: {performance['resource_diversity']}%")
    print(f"🎯 Unique Types Count: {performance['unique_types_count']}")
    print()
    
    # Type distribution
    print("📋 RESOURCE TYPE DISTRIBUTION:")
    for rtype, count in performance['resource_type_distribution'].items():
        percentage = (count / performance['total_resources']) * 100
        print(f"   {rtype.ljust(15)}: {count:3d} resources ({percentage:5.1f}%)")
    print()
    
    # Quality distribution
    quality_ranges = {
        'Excellent (90-100)': 0,
        'Great (80-89)': 0,
        'Good (70-79)': 0,
        'Average (60-69)': 0,
        'Below Average (<60)': 0
    }
    
    for resource in all_resources:
        quality = resource.get('quality_score', 0)
        if quality >= 90:
            quality_ranges['Excellent (90-100)'] += 1
        elif quality >= 80:
            quality_ranges['Great (80-89)'] += 1
        elif quality >= 70:
            quality_ranges['Good (70-79)'] += 1
        elif quality >= 60:
            quality_ranges['Average (60-69)'] += 1
        else:
            quality_ranges['Below Average (<60)'] += 1
    
    print("📊 QUALITY DISTRIBUTION:")
    for range_name, count in quality_ranges.items():
        if count > 0:
            percentage = (count / len(all_resources)) * 100
            print(f"   {range_name.ljust(20)}: {count:3d} resources ({percentage:5.1f}%)")
    print()
    
    # Recommendations
    print("💡 RECOMMENDATIONS:")
    for rec in performance.get('recommendations', []):
        print(f"   • {rec}")
    print()
    
    # Final assessment
    print("🎉 FINAL ASSESSMENT")
    print("=" * 80)
    
    total_per_subskill = len(all_resources) / len(subskills)
    print(f"📊 Average Resources per Subskill: {total_per_subskill:.1f}")
    
    if (performance['performance_grade'] in ['A+', 'A', 'A-'] and 
        performance['avg_quality_score'] >= 75 and
        total_per_subskill >= 6):
        print()
        print("🏆 EXCELLENT! Comprehensive resource system achieved!")
        print("   ✅ High average quality scores")
        print("   ✅ Many resources per subskill")
        print("   ✅ Good diversity of resource types")
        print("   ✅ Quality prioritized over speed")
    elif total_per_subskill >= 4:
        print()
        print("✅ GOOD! Resource system is working well")
        print(f"   ✅ {total_per_subskill:.1f} resources per subskill on average")
        print("   ⚠️  Some areas for improvement in quality/diversity")
    else:
        print()
        print("⚠️  NEEDS IMPROVEMENT")
        print(f"   📉 Only {total_per_subskill:.1f} resources per subskill")
        print("   🔧 Consider increasing resource fetching parameters")

if __name__ == "__main__":
    test_comprehensive_resources()
